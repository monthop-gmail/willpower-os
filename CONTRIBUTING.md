# 🪷 คู่มืออาสาสมัครนักพัฒนา (Contributor Guide)

> สำหรับอาสาสมัครทั่วประเทศที่ต้องการร่วมพัฒนา Willpower OS
> สถาบันพลังจิตตานุภาพ (Willpower Institute)

---

## 🙏 ยินดีต้อนรับ

ขอบคุณที่สนใจร่วมเป็นส่วนหนึ่งของโครงการ Willpower OS ทุกบรรทัดโค้ดที่คุณเขียนคือการช่วยเผยแผ่สมาธิสู่สากล

---

## 📖 อ่านก่อนเริ่มต้น (Required Reading)

1. **[AI_CONTEXT.md](./AI_CONTEXT.md)** — ธรรมนูญดิจิทัล (บังคับอ่าน)
2. **[README_DEV.md](./README_DEV.md)** — คู่มือนักพัฒนา
3. **[.cursorrules](./.cursorrules)** — กฎสำหรับ AI ที่ช่วยเขียนโค้ด

---

## 🔄 Git Flow

### Branch Strategy
```
main          ← Production (ห้าม push ตรง)
├── develop   ← Development branch (merge PR ที่นี่)
│   ├── feature/xxx   ← ฟีเจอร์ใหม่
│   ├── fix/xxx       ← แก้ Bug
│   └── docs/xxx      ← แก้เอกสาร
```

### ขั้นตอนการทำงาน

1. **Fork** repository
2. **Clone** มาที่เครื่อง
3. **สร้าง Branch** จาก `develop`
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```
4. **เขียนโค้ด** ตามมาตรฐาน
5. **Commit** ด้วย Conventional Commits
   ```bash
   git commit -m "feat: เพิ่มระบบบันทึกสมาธิ"
   ```
6. **Push** และเปิด **Pull Request** มาที่ `develop`
7. **รอ Review** จากทีมแกนกลางอย่างน้อย 1 ท่าน

### Commit Message Format
```
feat:     ← ฟีเจอร์ใหม่
fix:      ← แก้ Bug
docs:     ← แก้เอกสาร
refactor: ← ปรับโครงสร้าง (ไม่เปลี่ยนพฤติกรรม)
test:     ← เพิ่ม/แก้ Test
chore:    ← งานจิปาถะ (dependencies, config)
```

---

## 📏 Coding Standards

### JavaScript / TypeScript
- ใช้ **camelCase** สำหรับตัวแปรและฟังก์ชัน
- ใช้ **PascalCase** สำหรับ Component และ Class
- ทุกฟังก์ชันต้องมี **JSDoc** อธิบาย
- ใช้ **TypeScript** เท่านั้น (ห้ามใช้ `any` โดยไม่จำเป็น)

```typescript
/**
 * ดึงสถานะผู้ใช้จาก Supabase
 * @param userId - UUID ของผู้ใช้
 * @returns ข้อมูลสถานะผู้ใช้
 */
async function getUserStatus(userId: string): Promise<UserStatus> {
  // ...
}
```

### Python
- ใช้ **snake_case** สำหรับตัวแปรและฟังก์ชัน
- ใช้ **PascalCase** สำหรับ Class
- ทุกฟังก์ชันต้องมี **Docstring** อธิบาย
- ใช้ **Type Hints** เสมอ

```python
def get_user_status(user_id: str) -> dict:
    """
    ดึงสถานะผู้ใช้จาก Supabase

    Parameters:
        user_id: UUID ของผู้ใช้

    Returns:
        dict: ข้อมูลสถานะผู้ใช้
    """
    # ...
```

---

## 🛡️ AI Safety Rules

หากคุณทำงานกับ `willpower-os-ai`:

| กฎ | รายละเอียด |
|---|---|
| No Hallucination | AI ห้ามเดาคำตอบธรรมะ — ต้องดึงจาก RAG เท่านั้น |
| No Diagnosis | ห้ามวินิจฉัยสภาวะธรรม — แนะนำปรึกษาอาจารย์ |
| Source Required | ทุกคำตอบต้องอ้างอิง เล่ม/บท/หน้า |
| No New Content | ห้ามสร้างเนื้อหาธรรมะใหม่ |
| No Comparison | ห้ามเปรียบเทียบกับสำนักอื่น |

---

## 🔒 Data Privacy (PDPA)

- ❌ ห้าม Hard-code API Keys, Secrets, Passwords
- ❌ ห้าม Log ข้อมูลส่วนบุคคล (ชื่อจริง, เบอร์โทร, Line ID)
- ✅ ใช้ `.env` สำหรับทุก Secret
- ✅ ตรวจสอบว่า `.env` อยู่ใน `.gitignore`
- ✅ ข้อมูลส่วนบุคคลต้องเข้ารหัส
- ✅ ต้องมี Consent flow ก่อนเก็บข้อมูล

### Checklist ก่อน Push
- [ ] ไม่มี Secret ใน Code
- [ ] `.env` อยู่ใน `.gitignore`
- [ ] ไม่มี `console.log` ที่แสดงข้อมูลส่วนบุคคล
- [ ] มี Comment/Docstring ทุกฟังก์ชัน
- [ ] อัปเดต `docs/` หากแก้ API

---

## 🏗️ Tech Stack ที่ใช้

| Layer | Technology |
|---|---|
| Frontend | Next.js 14+ (TypeScript) |
| Backend (Core) | Node.js |
| Backend (AI) | FastAPI (Python 3.11+) |
| Database | Supabase (PostgreSQL + pgvector) |
| AI Model | Google Gemini 1.5 |
| Auth | Supabase Auth + Line Login |

> ⚠️ ห้ามเพิ่ม Library/Framework นอกเหนือจากนี้โดยไม่ปรึกษาทีมแกนกลาง

---

## ❓ มีคำถาม?

| เรื่อง | ช่องทาง |
|---|---|
| ปัญหาทางเทคนิค | เปิด Issue บน GitHub |
| เนื้อหาธรรมะ | ปรึกษาอาจารย์วิทยากร |
| การจัดการโครงการ | Line Group คณะอนุกรรมการ IT |

---

> 🪷 _สาธุ ขอบุญกุศลจากการพัฒนาระบบนี้ จงเป็นพลังส่งเสริมการเผยแผ่สมาธิสู่สากล_
