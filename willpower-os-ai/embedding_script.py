"""
🪷 Willpower OS AI — Embedding Script
สถาบันพลังจิตตานุภาพ (Willpower Institute)

Script สำหรับแปลงบทเรียนจากตำราหลักสูตรสมาธิ เป็น Vector Embedding
แล้วเก็บลงฐานข้อมูล Supabase (pgvector)

Usage:
    python embedding_script.py

Requirements:
    pip install google-generativeai supabase python-dotenv
"""

import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from supabase import create_client, Client

# โหลด Environment Variables
load_dotenv()

# ตั้งค่า Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("กรุณาตั้งค่า GEMINI_API_KEY ในไฟล์ .env")

genai.configure(api_key=GEMINI_API_KEY)

# ตั้งค่า Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    raise ValueError("กรุณาตั้งค่า SUPABASE_URL และ SUPABASE_SERVICE_ROLE_KEY ในไฟล์ .env")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

# ชื่อ Embedding Model ของ Gemini
EMBEDDING_MODEL = "models/embedding-001"

# ชื่อตารางใน Supabase สำหรับเก็บ Embedding
TABLE_NAME = "lesson_embeddings"


def create_embedding_table():
    """
    สร้างตาราง lesson_embeddings ใน Supabase (ถ้ายังไม่มี)
    ต้องรัน SQL นี้ใน Supabase SQL Editor ก่อน:

    CREATE TABLE lesson_embeddings (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        book_number INTEGER NOT NULL,
        chapter_number INTEGER NOT NULL,
        page_number INTEGER,
        title VARCHAR(500),
        content TEXT NOT NULL,
        embedding VECTOR(768),
        metadata JSONB,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

    CREATE INDEX idx_lesson_embeddings_embedding
        ON lesson_embeddings
        USING ivfflat (embedding vector_cosine_ops)
        WITH (lists = 100);
    """
    print("กรุณาตรวจสอบว่าตาราง lesson_embeddings ถูกสร้างใน Supabase แล้ว")
    print("ดู SQL ใน docstring ของฟังก์ชัน create_embedding_table()")


def generate_embedding(text: str) -> list[float]:
    """
    แปลงข้อความเป็น Vector Embedding ด้วย Gemini API

    Parameters:
        text: ข้อความที่ต้องการแปลง

    Returns:
        list[float]: Vector embedding (768 dimensions)
    """
    result = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=text,
        task_type="retrieval_document"
    )
    return result["embedding"]


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    """
    แบ่งข้อความยาวเป็นชิ้นเล็กๆ (chunks) เพื่อทำ Embedding

    Parameters:
        text: ข้อความต้นฉบับ
        chunk_size: ขนาดแต่ละ chunk (จำนวนตัวอักษร)
        overlap: จำนวนตัวอักษรที่ซ้อนทับกันระหว่าง chunk

    Returns:
        list[str]: รายการ chunks
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk.strip())
        start = end - overlap
    return [c for c in chunks if c]


def embed_and_store(
    content: str,
    book_number: int,
    chapter_number: int,
    page_number: int = None,
    title: str = None
):
    """
    แปลงเนื้อหาบทเรียนเป็น Embedding และเก็บลง Supabase

    Parameters:
        content: เนื้อหาบทเรียน
        book_number: เล่มที่ (1-3)
        chapter_number: บทที่
        page_number: หน้าที่ (optional)
        title: ชื่อบท/หัวข้อ (optional)
    """
    # แบ่งเนื้อหาเป็น chunks
    chunks = chunk_text(content)

    print(f"กำลังประมวลผล: เล่ม {book_number}, บทที่ {chapter_number} ({len(chunks)} chunks)")

    for i, chunk in enumerate(chunks):
        # สร้าง Embedding
        embedding = generate_embedding(chunk)

        # เก็บลง Supabase
        record = {
            "book_number": book_number,
            "chapter_number": chapter_number,
            "page_number": page_number,
            "title": title or f"เล่ม {book_number} บทที่ {chapter_number}",
            "content": chunk,
            "embedding": embedding,
            "metadata": json.dumps({
                "chunk_index": i,
                "total_chunks": len(chunks),
                "source": f"ตำราหลักสูตรสมาธิ เล่ม {book_number}"
            })
        }

        supabase.table(TABLE_NAME).insert(record).execute()
        print(f"  ✓ Chunk {i + 1}/{len(chunks)} เก็บเรียบร้อย")

    print(f"  ✅ เล่ม {book_number}, บทที่ {chapter_number} เสร็จสมบูรณ์\n")


def search_similar(query: str, top_k: int = 5) -> list[dict]:
    """
    ค้นหาเนื้อหาที่ใกล้เคียงกับคำถาม (Vector Similarity Search)

    Parameters:
        query: คำถามของผู้ใช้
        top_k: จำนวนผลลัพธ์ที่ต้องการ

    Returns:
        list[dict]: รายการเนื้อหาที่เกี่ยวข้อง พร้อม similarity score
    """
    # สร้าง Embedding สำหรับคำถาม
    query_embedding = generate_embedding(query)

    # ค้นหาด้วย pgvector (ต้องสร้าง RPC function ใน Supabase)
    # SQL: SELECT *, 1 - (embedding <=> query_embedding) AS similarity
    #      FROM lesson_embeddings ORDER BY similarity DESC LIMIT top_k
    result = supabase.rpc(
        "match_lessons",
        {
            "query_embedding": query_embedding,
            "match_threshold": 0.7,
            "match_count": top_k
        }
    ).execute()

    return result.data


# =====================================================
# ตัวอย่างการใช้งาน (Example Usage)
# =====================================================

if __name__ == "__main__":
    print("=" * 60)
    print("🪷 Willpower OS — Embedding Script")
    print("   สถาบันพลังจิตตานุภาพ")
    print("=" * 60)
    print()

    # ตรวจสอบว่าตาราง Embedding พร้อมใช้งาน
    create_embedding_table()
    print()

    # =====================================================
    # ตัวอย่าง: Embed บทเรียนเล่ม 1 บทที่ 1
    # ในการใช้งานจริง ให้โหลดเนื้อหาจากไฟล์ตำรา
    # =====================================================

    sample_lesson = """
    สมาธิ คือ ความตั้งมั่นของจิต เป็นคุณธรรมที่สำคัญยิ่งประการหนึ่ง
    ในพระพุทธศาสนา หลวงพ่อวิริยังค์ สิรินฺธโร ได้สอนวิธีการทำสมาธิ
    โดยเริ่มจากการนั่งสมาธิเบื้องต้น ด้วยการกำหนดลมหายใจเข้าออก
    และบริกรรมภาวนาว่า "สัมมา อะระหัง"

    (หมายเหตุ: นี่คือข้อความตัวอย่างสำหรับทดสอบระบบ Embedding เท่านั้น
    ในการใช้งานจริง ให้ใช้เนื้อหาจากตำราหลักสูตรสมาธิฉบับจริง)
    """

    print("📖 กำลังทดสอบ Embedding ด้วยข้อความตัวอย่าง...")
    print()

    try:
        embed_and_store(
            content=sample_lesson,
            book_number=1,
            chapter_number=1,
            page_number=1,
            title="บทนำ: สมาธิเบื้องต้น"
        )
        print("🎉 ทดสอบ Embedding สำเร็จ!")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        print("กรุณาตรวจสอบ:")
        print("  1. GEMINI_API_KEY ถูกต้อง")
        print("  2. SUPABASE_URL และ SUPABASE_SERVICE_ROLE_KEY ถูกต้อง")
        print("  3. ตาราง lesson_embeddings ถูกสร้างใน Supabase แล้ว")

    print()
    print("=" * 60)
    print("เสร็จสิ้น")
    print("=" * 60)
