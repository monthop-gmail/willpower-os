# 🪷 Willpower OS — ธรรมนูญดิจิทัล (Digital Constitution)

> **เอกสารฉบับนี้คือ "เข็มทิศหลัก" ของโครงการ Willpower OS**
> AI และ Developer ทุกคนต้องอ่านและปฏิบัติตามอย่างเคร่งครัด
> (Zero-Inference & Strict Governance)

---

## 1. อัตลักษณ์ระบบ (System Identity)

| หัวข้อ | รายละเอียด |
|---|---|
| **ชื่อโครงการ** | Willpower OS (ระบบปฏิบัติการพลังจิตตานุภาพ) |
| **องค์กร** | สถาบันพลังจิตตานุภาพ (samathi101.com) |
| **ผู้ก่อตั้ง** | พระธรรมมงคลญาณ (หลวงพ่อวิริยังค์ สิรินฺธโร) |
| **วิสัยทัศน์** | เชื่อมโยงพลังจิตไทย สู่สมาธิโลก ด้วยระบบปฏิบัติการดิจิทัลอัจฉริยะ |
| **เป้าหมายหลัก** | ความถูกต้องของคำสอน 100% และการสะสมพลังจิต (Meditation Minutes) |

### 1.1 คุณค่าหลัก (Core Values)
- **ความถูกต้อง (Accuracy):** คำสอนทุกคำต้องตรงตามตำราหลักสูตรเล่ม 1-3 เท่านั้น
- **ความสำรวม (Mindfulness):** ทุกสิ่งที่สร้างต้องสะท้อนความนอบน้อมและเมตตา
- **การสะสมพลังจิต (Merit):** ระบบต้องส่งเสริมให้ผู้ใช้ปฏิบัติสมาธิอย่างสม่ำเสมอ
- **ความปลอดภัย (Privacy):** ข้อมูลส่วนบุคคลของผู้ปฏิบัติต้องได้รับการคุ้มครองตาม PDPA

### 1.2 กลุ่มเป้าหมาย (Target Users)
- นักศึกษาครูสมาธิ (หลักสูตรเล่ม 1-3)
- อาจารย์วิทยากร
- พี่เลี้ยงสมาธิ
- คณะอนุกรรมการ IT (แกนกลาง 8 ท่าน)
- อาสาสมัครนักพัฒนาทั่วประเทศ

---

## 2. บุคลิกภาพ AI (AI Personality & Tone of Voice)

### 2.1 บุคลิกที่ต้องมี
- **สำรวม** — ใช้ภาษาสุภาพ ไม่หยาบกระด้าง ไม่ใช้คำแสลง
- **นอบน้อม** — ให้เกียรติผู้ถาม ใช้ครับ/ค่ะ
- **เมตตา** — ตอบด้วยความปรารถนาดี แม้คำถามจะซ้ำหรือพื้นฐาน
- **อ้างอิงได้** — ทุกคำตอบต้องระบุแหล่งที่มา (เล่ม/บท/หน้า)

### 2.2 ตัวอย่างการตอบที่ถูกต้อง
```
ผู้ถาม: "สมาธิแบบหลวงพ่อต่างจากวิปัสสนาสายอื่นอย่างไร?"

AI: "ขออภัยครับ ผมไม่สามารถเปรียบเทียบกับสำนักอื่นได้
เนื่องจากระบบนี้ออกแบบมาเพื่ออธิบายคำสอนของหลวงพ่อวิริยังค์โดยเฉพาะ
แนะนำให้ปรึกษาอาจารย์วิทยากรประจำสาขาของท่านครับ"
```

### 2.3 ตัวอย่างการตอบที่ห้ามทำ
```
❌ "สมาธิหลวงพ่อดีกว่าสำนักอื่นเพราะ..."
❌ "ผมคิดว่าสภาวะที่คุณเจอน่าจะเป็นฌานที่ 2..."
❌ "ลองทำแบบนี้แทนก็ได้ ผมเห็นว่าน่าจะดีกว่า..."
```

---

## 3. กฎเหล็กทางเทคนิค (Technical Constraints)

### 3.1 Tech Stack — ห้ามเปลี่ยนโดยไม่ผ่านอนุมัติ

| Layer | Technology | หมายเหตุ |
|---|---|---|
| **Frontend** | Next.js (App Router) | TypeScript เท่านั้น |
| **Backend** | FastAPI (Python) | สำหรับ AI Services |
| **Backend** | Node.js (Express/Hono) | สำหรับ Core API (ทางเลือก) |
| **Database** | Supabase (PostgreSQL) | Managed, มี Row Level Security |
| **Vector DB** | pgvector (Supabase) | สำหรับ RAG Embedding |
| **AI Model** | Google Gemini 1.5 Pro/Flash | ห้ามใช้ Model อื่นโดยไม่อนุมัติ |
| **Auth** | Supabase Auth + Line Login | Single Sign-On (Willpower ID) |
| **Hosting** | Vercel / Cloud Run | ตาม Repo |

### 3.2 Architecture — Micro-repositories

```
willpower-os/
├── willpower-os-core/     ← ระบบประสาทส่วนกลาง
│   ├── src/
│   ├── database_schema.sql
│   ├── core_api_spec.yaml
│   └── README.md
│
├── willpower-os-ai/       ← สมอง AI
│   ├── src/
│   ├── ai_system_prompt.txt
│   ├── embedding_script.py
│   ├── ai_api_spec.yaml
│   └── README.md
│
├── .cursorrules           ← กฎสำหรับ AI Assistant
├── AI_CONTEXT.md          ← ธรรมนูญดิจิทัลฉบับนี้
├── README_DEV.md          ← คู่มือ Developer
└── CONTRIBUTING.md        ← คู่มืออาสาสมัคร
```

### 3.3 Database Schema — บังคับใช้ตามนี้

#### ตาราง `users`
| Column | Type | Description |
|---|---|---|
| `id` | UUID (PK) | รหัสผู้ใช้ (Auto-generated) |
| `line_id` | VARCHAR | Line User ID สำหรับ Login |
| `display_name` | VARCHAR | ชื่อที่แสดง |
| `branch_id` | UUID (FK) | สาขาที่สังกัด |
| `student_status` | ENUM | สถานะ: `enrolled`, `graduated`, `instructor` |
| `role` | ENUM | บทบาท: `student`, `mentor`, `instructor`, `admin` |
| `pdpa_consent` | BOOLEAN | ยินยอม PDPA แล้วหรือไม่ |
| `created_at` | TIMESTAMP | วันที่สร้างบัญชี |
| `updated_at` | TIMESTAMP | วันที่อัปเดตล่าสุด |

#### ตาราง `meditation_logs`
| Column | Type | Description |
|---|---|---|
| `id` | UUID (PK) | รหัส Log |
| `user_id` | UUID (FK) | เจ้าของ Log |
| `type` | ENUM | ประเภท: `sitting` (นั่งสมาธิ), `walking` (เดินจงกรม) |
| `duration_minutes` | INTEGER | จำนวนนาที |
| `session_date` | DATE | วันที่ปฏิบัติ |
| `note` | TEXT | บันทึกสภาวะ (optional) |
| `logged_at` | TIMESTAMP | วันเวลาที่บันทึก |

#### ตาราง `branches`
| Column | Type | Description |
|---|---|---|
| `id` | UUID (PK) | รหัสสาขา |
| `name` | VARCHAR | ชื่อสาขา |
| `region` | VARCHAR | ภูมิภาค |
| `address` | TEXT | ที่อยู่ |
| `is_active` | BOOLEAN | เปิด/ปิดสาขา |
| `created_at` | TIMESTAMP | วันที่สร้าง |

#### ตาราง `lecture_tapes`
| Column | Type | Description |
|---|---|---|
| `id` | UUID (PK) | รหัสเทป |
| `book_number` | INTEGER | เล่มที่ (1-3) |
| `chapter_number` | INTEGER | บทที่ |
| `tape_code` | VARCHAR | รหัสม้วนเทป เช่น "T1-01" |
| `title` | VARCHAR | ชื่อเทป/หัวข้อบรรยาย |
| `version` | INTEGER | version (1 = ต้นฉบับ, 2+ = ปรับปรุง) |
| `is_latest` | BOOLEAN | เป็น version ล่าสุดหรือไม่ |
| `transcription` | TEXT | เนื้อหาถอดเสียง |
| `duration_seconds` | INTEGER | ความยาวเทป (วินาที) |
| `recorded_date` | DATE | วันที่บรรยาย |
| `lecturer` | VARCHAR | ผู้บรรยาย |
| `notes` | TEXT | หมายเหตุการปรับปรุง |

> **หมายเหตุ:** 1 บท = 1 ม้วนหลัก แต่อาจมีหลาย version (ปรับปรุง) — version เก่าเก็บไว้อ้างอิง

#### ตาราง `courses`
| Column | Type | Description |
|---|---|---|
| `id` | UUID (PK) | รหัสหลักสูตร |
| `code` | VARCHAR (UNIQUE) | รหัสย่อ เช่น "CHIN1", "KRU", "WITAN" |
| `name` | VARCHAR | ชื่อหลักสูตร |
| `description` | TEXT | คำอธิบาย |
| `target_audience` | VARCHAR | กลุ่มเป้าหมาย |
| `total_hours` | INTEGER | ชั่วโมงเรียนโดยประมาณ |
| `sort_order` | INTEGER | ลำดับการแสดงผล |

> **หลักสูตรที่มี:** ชินสาสมาธิ #1 (10 บท), ชินสาสมาธิ #2 (5 บท), ครูสมาธิ (เล่ม 1-3 เต็ม), วิทันตสาสมาธิ (เล่ม 1-3 + สื่อบรรยายเฉพาะ)

#### ตาราง `course_chapters`
| Column | Type | Description |
|---|---|---|
| `id` | UUID (PK) | รหัส |
| `course_id` | UUID (FK) | หลักสูตร |
| `book_number` | INTEGER | เล่มที่ (1-3) |
| `chapter_number` | INTEGER | บทที่ |
| `sort_order` | INTEGER | ลำดับการสอนในหลักสูตรนี้ |
| `is_required` | BOOLEAN | บทบังคับ หรือ บทเสริม |

#### ตาราง `teaching_materials`
| Column | Type | Description |
|---|---|---|
| `id` | UUID (PK) | รหัสสื่อ |
| `course_id` | UUID (FK) | หลักสูตร |
| `course_chapter_id` | UUID (FK, nullable) | ผูกกับบทเฉพาะ (null = สื่อทั่วไปของหลักสูตร) |
| `type` | ENUM | ประเภท: `slide`, `handout`, `video`, `audio`, `guide`, `exercise`, `other` |
| `title` | VARCHAR | ชื่อสื่อ |
| `file_url` | TEXT | URL ไฟล์ |
| `version` | INTEGER | version ของสื่อ |
| `is_latest` | BOOLEAN | เป็น version ล่าสุดหรือไม่ |
| `uploaded_by` | UUID (FK) | ผู้อัปโหลด |

> **หมายเหตุ:** แต่ละหลักสูตรมีชุดสื่อการสอนของตัวเอง — ครูสมาธิ vs วิทันตสาสมาธิ ใช้ตำราเดียวกันแต่ชุดสื่อบรรยายต่างกัน

### 3.4 API Standard

ทุก API ต้องสื่อสารผ่าน JSON format ตาม Spec ที่กำหนด:

**Core API Endpoints:**
```
GET  /api/v1/users/{id}/status     → สถานะผู้ใช้
POST /api/v1/logs/meditation       → บันทึกการปฏิบัติ
GET  /api/v1/branches              → รายชื่อสาขา
```

**AI API Endpoints:**
```
POST /api/v1/ai/ask                → ถาม AI (RAG)
POST /api/v1/ai/feedback           → ส่ง Feedback (👍/👎)
```

**Response Format มาตรฐาน:**
```json
{
  "success": true,
  "data": { },
  "error": null,
  "metadata": {
    "timestamp": "2026-03-18T10:00:00Z",
    "version": "1.0.0"
  }
}
```

---

## 4. มาตรฐานการเขียน Code (Coding Standards)

### 4.1 Naming Convention
| ภาษา | รูปแบบ | ตัวอย่าง |
|---|---|---|
| JavaScript / TypeScript | camelCase | `getUserStatus`, `meditationLog` |
| Python | snake_case | `get_user_status`, `meditation_log` |
| Database Columns | snake_case | `branch_id`, `created_at` |
| Environment Variables | UPPER_SNAKE | `SUPABASE_URL`, `GEMINI_API_KEY` |
| Files (JS/TS) | kebab-case | `user-profile.tsx`, `api-handler.ts` |
| Files (Python) | snake_case | `embedding_script.py` |

### 4.2 Documentation
- ทุก Function **ต้องมี** Comment/Docstring อธิบาย:
  - จุดประสงค์ของ Function
  - Parameters และ Return type
- เมื่อแก้ไข API ต้องอัปเดตไฟล์ใน `docs/` เสมอ
- Commit message ใช้ Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`

### 4.3 Security — กฎเด็ดขาด
- ❌ **ห้าม** Hard-code API Keys, Secrets, Passwords ในโค้ด
- ✅ ใช้ `.env` และ Environment Variables เท่านั้น
- ✅ ไฟล์ `.env` ต้องอยู่ใน `.gitignore` เสมอ
- ✅ ข้อมูลส่วนบุคคลต้องเข้ารหัส (Encryption at rest & in transit)
- ✅ ต้องมี PDPA Consent ก่อนเก็บข้อมูลผู้ใช้
- ❌ **ห้าม** Log ข้อมูลส่วนบุคคลใน Console/Debug output

---

## 5. AI Guardrails — กฎการตรวจสอบ AI

### 5.1 กฎ 5 ข้อที่ห้ามละเมิด

| # | กฎ | เหตุผล |
|---|---|---|
| 1 | **ห้ามเดาคำตอบธรรมะ** | คำสอนต้องถูกต้อง 100% ห้าม Hallucinate |
| 2 | **ห้ามวินิจฉัยสภาวะธรรม** | เป็นหน้าที่ของอาจารย์วิทยากรเท่านั้น |
| 3 | **ต้องมี Source Reference** | ทุกคำตอบต้องอ้างอิง เล่ม/บท/หน้า |
| 4 | **ห้ามสร้างเนื้อหาธรรมะใหม่** | ใช้เฉพาะข้อมูลจากตำราเล่ม 1-3 |
| 5 | **ห้ามเปรียบเทียบกับสำนักอื่น** | ระบบนี้เฉพาะคำสอนหลวงพ่อวิริยังค์ |

### 5.2 เมื่อ AI ไม่แน่ใจ — ให้ทำตามขั้นตอนนี้

```
1. แจ้งผู้ถามว่า "ข้อมูลนี้ยังไม่สามารถยืนยันได้ในระบบ"
2. แนะนำให้ปรึกษา "อาจารย์วิทยากร" ประจำสาขา
3. บันทึกคำถามนี้เข้าระบบ Feedback เพื่อให้ทีมเนื้อหาตรวจสอบ
4. ห้ามเดาหรือตอบจากความรู้ทั่วไป
```

### 5.3 ขอบเขตข้อมูลที่ AI เข้าถึงได้

| แหล่งข้อมูล | สถานะ |
|---|---|
| ตำราหลักสูตรสมาธิ เล่ม 1 | ✅ อนุญาต |
| ตำราหลักสูตรสมาธิ เล่ม 2 | ✅ อนุญาต |
| ตำราหลักสูตรสมาธิ เล่ม 3 | ✅ อนุญาต |
| เทปบรรยายประจำบท (Lecture Tapes) | ✅ อนุญาต — ใช้ version ล่าสุดเป็นหลัก, version เก่าใช้เสริมได้ (ระบุ version กำกับ) |
| หนังสือ/บทความ ภายนอกสถาบัน | ❌ ห้ามใช้ |
| ความรู้ทั่วไปของ AI Model | ❌ ห้ามใช้ตอบเรื่องธรรมะ |
| ข้อมูลประชาสัมพันธ์สถาบัน | ✅ อนุญาต (สำหรับข้อมูลทั่วไป) |

---

## 6. Roadmap อ้างอิง (จาก Digital Master Plan)

| ปี | ระยะ | เป้าหมายหลัก |
|---|---|---|
| **ปีที่ 1 (2026)** | Foundation | Willpower ID, Meditation Tracker, AI RAG MVP |
| **ปีที่ 2 (2027)** | Scaling | Multi-language, Branch Management, Gamification |
| **ปีที่ 3 (2028)** | Global | Global Platform, Video Indexing, Executive Dashboard |

---

## 📌 หมายเหตุสำคัญ

> **เอกสารฉบับนี้มีผลบังคับใช้กับทุกคนที่เข้ามาพัฒนา Willpower OS**
> หากต้องการแก้ไขหรือเพิ่มเติม ต้องผ่านการอนุมัติจากคณะอนุกรรมการ IT
> ฉบับปัจจุบัน: v1.0.0 | วันที่: 2026-03-18
