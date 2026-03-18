# 🪷 Willpower OS — คู่มือนักพัฒนา (Developer Guide)

> สำหรับ Developer ทุกท่านที่เข้ามาร่วมพัฒนาโครงการ Willpower OS
> กรุณาอ่านเอกสารนี้ให้จบก่อนเริ่มเขียนโค้ด

---

## 🚀 เริ่มต้นอย่างรวดเร็ว (Quick Start)

### 1. ทำความเข้าใจโครงการ
- อ่าน [AI_CONTEXT.md](./AI_CONTEXT.md) — ธรรมนูญดิจิทัล (บังคับอ่าน)
- ทำความเข้าใจ `.cursorrules` — กฎสำหรับ AI ที่ช่วย Code

### 2. โครงสร้าง Repository

```
willpower-os/
├── willpower-os-core/          ← ระบบประสาทส่วนกลาง
│   ├── src/                    ← Source code (Next.js / Node.js)
│   ├── database_schema.sql     ← โครงสร้าง Database
│   ├── core_api_spec.yaml      ← API Spec (OpenAPI)
│   └── README.md
│
├── willpower-os-ai/            ← สมอง AI
│   ├── src/                    ← Source code (FastAPI / Python)
│   ├── ai_system_prompt.txt    ← System Prompt สำหรับ AI
│   ├── embedding_script.py     ← Script ทำ Embedding
│   ├── ai_api_spec.yaml        ← API Spec (OpenAPI)
│   └── README.md
│
├── .cursorrules                ← AI Rules
├── AI_CONTEXT.md               ← ธรรมนูญดิจิทัล
├── README_DEV.md               ← คุณอยู่ที่นี่
└── CONTRIBUTING.md             ← คู่มืออาสาสมัคร
```

---

## 🛠️ Tech Stack

| Layer | Technology | Version |
|---|---|---|
| Frontend | Next.js (App Router) | 14+ |
| Backend (Core) | Node.js / Express / Hono | 20+ LTS |
| Backend (AI) | FastAPI (Python) | 3.11+ |
| Database | Supabase (PostgreSQL) | Latest |
| Vector Store | pgvector (Supabase) | Latest |
| AI Model | Google Gemini 1.5 Pro/Flash | Latest |
| Auth | Supabase Auth + Line Login | - |

> ⚠️ **ห้ามเพิ่ม Tech Stack นอกเหนือจากนี้โดยไม่ผ่านการอนุมัติจากคณะอนุกรรมการ IT**

---

## 📏 มาตรฐานการเขียนโค้ด (Coding Standards)

### Naming Convention

```javascript
// JavaScript / TypeScript → camelCase
const userName = "สมชาย";
function getMeditationLog(userId) { ... }
```

```python
# Python → snake_case
user_name = "สมชาย"
def get_meditation_log(user_id): ...
```

### Commit Message — ใช้ Conventional Commits

```
feat: เพิ่มระบบบันทึกการนั่งสมาธิ
fix: แก้ไขการคำนวณนาทีสะสม
docs: อัปเดต API Spec สำหรับ /ai/ask
refactor: ปรับโครงสร้าง embedding pipeline
```

### Git Flow

```
main          ← Production (ห้าม push ตรง)
├── develop   ← Development branch
│   ├── feature/meditation-tracker
│   ├── feature/ai-rag-engine
│   └── fix/login-line-id
```

- สร้าง Branch จาก `develop` เสมอ
- ตั้งชื่อ Branch: `feature/ชื่อ-feature` หรือ `fix/ชื่อ-bug`
- เปิด Pull Request → ต้องมีอย่างน้อย 1 Reviewer approve

---

## 🔒 Security Checklist

ก่อน Commit ทุกครั้ง ตรวจสอบว่า:

- [ ] ไม่มี API Key, Secret, Password ใน Code
- [ ] `.env` อยู่ใน `.gitignore`
- [ ] ไม่มี `console.log` ที่แสดงข้อมูลส่วนบุคคล
- [ ] ถ้าเก็บข้อมูลผู้ใช้ → มี PDPA Consent flow
- [ ] ข้อมูลส่วนบุคคลถูกเข้ารหัส

---

## 🤖 สำหรับ AI Developer

หากคุณทำงานกับ `willpower-os-ai` ต้องปฏิบัติตาม AI Guardrails:

1. **ห้ามเดาคำตอบธรรมะ** — ใช้ RAG ดึงจากตำราเท่านั้น
2. **ห้ามวินิจฉัยสภาวะธรรม** — แนะนำปรึกษาอาจารย์วิทยากร
3. **ทุกคำตอบต้องมี Reference** — เล่ม/บท/หน้า
4. **ห้ามสร้างเนื้อหาธรรมะใหม่** — ตำราเล่ม 1-3 เท่านั้น
5. **ห้ามเปรียบเทียบสำนัก** — เฉพาะคำสอนหลวงพ่อวิริยังค์

---

## 📡 API Response มาตรฐาน

ทุก API ต้องตอบกลับในรูปแบบนี้:

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

กรณี Error:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "UNAUTHORIZED",
    "message": "กรุณาเข้าสู่ระบบก่อนใช้งาน"
  },
  "metadata": {
    "timestamp": "2026-03-18T10:00:00Z",
    "version": "1.0.0"
  }
}
```

---

## 🆘 ติดต่อทีม

| บทบาท | ช่องทาง |
|---|---|
| คณะอนุกรรมการ IT | Line Group (แกนกลาง 15 ท่าน) |
| ปัญหาทางเทคนิค | GitHub Issues |
| เนื้อหาธรรมะ | ปรึกษาอาจารย์วิทยากรประจำสาขา |

---

> 🪷 _"ทุกบรรทัดโค้ดที่เราเขียน คือการสร้างบุญกุศลเพื่อเผยแผ่สมาธิสู่สากล"_
>
> — โครงการ Willpower OS, สถาบันพลังจิตตานุภาพ
