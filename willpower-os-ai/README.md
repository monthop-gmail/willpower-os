# 🪷 Willpower OS AI — สมอง AI

> AI Engine ของ Willpower OS
> จัดการ RAG Engine, Embedding Pipeline, Prompt Management และ Transcription

---

## 📋 ภาพรวม

`willpower-os-ai` คือ AI Backend ที่ทำหน้าที่:
- **RAG Engine:** ค้นหาคำตอบจากตำราเล่ม 1-3 และเทปบรรยายด้วย Vector Search (แยก source_type: textbook/lecture_tape)
- **Embedding Pipeline:** แปลงเนื้อหาตำราและ transcription เทปบรรยายเป็น Vector เก็บใน pgvector
- **Lecture Tape Processing:** ประมวลผล transcription จากเทปบรรยาย รองรับหลาย version
- **Prompt Management:** จัดการ System Prompt ให้ AI มีบุคลิกสำรวม นอบน้อม
- **Feedback System:** เก็บ 👍/👎 เพื่อปรับปรุงคุณภาพคำตอบ

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Runtime | Python 3.11+ |
| Framework | FastAPI |
| AI Model | Google Gemini 1.5 Pro/Flash |
| Vector Store | pgvector (Supabase) |
| Embedding | Gemini Embedding API |
| Database | Supabase (PostgreSQL) |

---

## 📁 โครงสร้างโปรเจกต์

```
willpower-os-ai/
├── src/
│   ├── main.py               ← FastAPI entry point
│   ├── routers/
│   │   ├── ask.py             ← POST /ai/ask
│   │   └── feedback.py        ← POST /ai/feedback
│   ├── services/
│   │   ├── rag_engine.py      ← RAG logic (retrieve + generate)
│   │   ├── embedding.py       ← Embedding service
│   │   └── gemini_client.py   ← Gemini API wrapper
│   └── config.py              ← Settings & env vars
├── ai_system_prompt.txt        ← System prompt สำหรับ AI
├── embedding_script.py         ← Script ทำ Embedding ข้อมูลตำรา + เทปบรรยาย
├── ai_api_spec.yaml            ← OpenAPI spec
├── requirements.txt            ← Python dependencies
├── docs/                       ← Documentation
├── .env.example                ← Environment variables template
└── README.md
```

---

## 🚀 การติดตั้ง (Installation)

### 1. Clone repository
```bash
git clone https://github.com/willpower-os/willpower-os-ai.git
cd willpower-os-ai
```

### 2. สร้าง Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
```

### 3. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 4. ตั้งค่า Environment Variables
```bash
cp .env.example .env
```

แก้ไขไฟล์ `.env`:
```env
GEMINI_API_KEY=your-gemini-api-key
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

### 5. ทำ Embedding ข้อมูลตำรา (ครั้งแรก)
```bash
python embedding_script.py
```

### 6. รัน Development Server
```bash
uvicorn src.main:app --reload --port 8000
```

เปิด http://localhost:8000/docs (Swagger UI)

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/ai/ask` | ถามคำถาม → RAG ค้นหา → ตอบพร้อมอ้างอิง |
| `POST` | `/api/v1/ai/feedback` | ส่ง Feedback (👍/👎) ต่อคำตอบ |

ดู Spec เต็มที่ `ai_api_spec.yaml`

---

## 🛡️ AI Guardrails

1. ห้ามเดาคำตอบธรรมะ — ใช้ RAG ดึงจากตำราและเทปบรรยายเท่านั้น
2. ห้ามวินิจฉัยสภาวะธรรม — แนะนำปรึกษาอาจารย์วิทยากร
3. ทุกคำตอบต้องระบุ source_type + Reference:
   - จากตำรา: `[อ้างอิง: ตำราเล่ม X, บทที่ Y, หน้า Z]`
   - จากเทปบรรยาย: `[อ้างอิง: เทปบรรยาย เล่ม X, บทที่ Y, รหัส T-XX (v.N)]`
4. ห้ามสร้างเนื้อหาธรรมะใหม่
5. ห้ามเปรียบเทียบกับสำนักอื่น

ดูรายละเอียดใน `ai_system_prompt.txt`

---

## 🧪 การทดสอบ

```bash
# ทดสอบ Embedding
python -m pytest tests/test_embedding.py

# ทดสอบ RAG
python -m pytest tests/test_rag.py

# ทดสอบ API
python -m pytest tests/test_api.py
```

---

> 🪷 สถาบันพลังจิตตานุภาพ | Willpower OS AI v1.0.0
