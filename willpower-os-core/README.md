# 🪷 Willpower OS Core — ระบบประสาทส่วนกลาง

> Central Nervous System ของ Willpower OS
> จัดการ User, Auth, Branch Data, สถิติการปฏิบัติสมาธิ และ Universal API

---

## 📋 ภาพรวม

`willpower-os-core` คือ Backend หลักของระบบ Willpower OS ทำหน้าที่:
- **User Management:** ระบบ Willpower ID (Line Login + Supabase Auth)
- **Meditation Tracking:** บันทึกนาทีนั่งสมาธิ/เดินจงกรม
- **Branch Management:** จัดการข้อมูลสาขาทั่วประเทศ
- **API Gateway:** จุดเชื่อมต่อกลางสำหรับทุก Service

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Runtime | Node.js 20+ LTS |
| Framework | Next.js 14+ (App Router) |
| Database | Supabase (PostgreSQL + pgvector) |
| Auth | Supabase Auth + Line Login |
| API Spec | OpenAPI 3.0 (core_api_spec.yaml) |
| Hosting | Vercel |

---

## 📁 โครงสร้างโปรเจกต์

```
willpower-os-core/
├── src/
│   ├── app/                  ← Next.js App Router
│   │   ├── api/
│   │   │   ├── users/        ← User endpoints
│   │   │   ├── logs/         ← Meditation log endpoints
│   │   │   └── branches/     ← Branch endpoints
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── lib/
│   │   ├── supabase.ts       ← Supabase client
│   │   └── auth.ts           ← Auth helpers
│   └── types/
│       └── index.ts          ← TypeScript interfaces
├── database_schema.sql        ← Database schema
├── core_api_spec.yaml         ← OpenAPI spec
├── docs/                      ← Documentation
├── .env.example               ← Environment variables template
├── package.json
└── README.md
```

---

## 🚀 การติดตั้ง (Installation)

### 1. Clone repository
```bash
git clone https://github.com/willpower-os/willpower-os-core.git
cd willpower-os-core
```

### 2. ติดตั้ง Dependencies
```bash
npm install
```

### 3. ตั้งค่า Environment Variables
```bash
cp .env.example .env
```

แก้ไขไฟล์ `.env`:
```env
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
LINE_CHANNEL_ID=your-line-channel-id
LINE_CHANNEL_SECRET=your-line-channel-secret
```

### 4. สร้าง Database
นำไฟล์ `database_schema.sql` ไปรันใน Supabase SQL Editor

### 5. รัน Development Server
```bash
npm run dev
```

เปิด http://localhost:3000

---

## 📡 API Endpoints หลัก

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/users/{id}/status` | ดึงสถานะผู้ใช้ |
| `POST` | `/api/v1/logs/meditation` | บันทึกการปฏิบัติสมาธิ |
| `GET` | `/api/v1/branches` | รายชื่อสาขาทั้งหมด |
| `GET` | `/api/v1/branches/{id}` | รายละเอียดสาขา |

ดู Spec เต็มที่ `core_api_spec.yaml`

---

## 🔒 Security

- ห้าม Hard-code API Keys — ใช้ `.env` เท่านั้น
- Row Level Security (RLS) เปิดใช้งานใน Supabase
- ข้อมูลส่วนบุคคลเข้ารหัส ปฏิบัติตาม PDPA
- ทุก Request ต้องผ่าน Authentication (ยกเว้น Public endpoints)

---

> 🪷 สถาบันพลังจิตตานุภาพ | Willpower OS v1.0.0
