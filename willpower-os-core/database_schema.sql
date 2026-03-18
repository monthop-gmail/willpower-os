-- =====================================================
-- 🪷 Willpower OS Core — Database Schema
-- สถาบันพลังจิตตานุภาพ (Willpower Institute)
-- Database: Supabase (PostgreSQL + pgvector)
-- =====================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgvector";

-- =====================================================
-- ENUM Types
-- =====================================================

CREATE TYPE student_status AS ENUM (
    'enrolled',     -- กำลังศึกษา
    'graduated',    -- สำเร็จหลักสูตร
    'instructor'    -- เป็นวิทยากรแล้ว
);

CREATE TYPE user_role AS ENUM (
    'student',      -- นักศึกษา
    'mentor',       -- พี่เลี้ยง
    'instructor',   -- วิทยากร
    'admin'         -- ผู้ดูแลระบบ
);

CREATE TYPE meditation_type AS ENUM (
    'sitting',      -- นั่งสมาธิ
    'walking'       -- เดินจงกรม
);

-- =====================================================
-- Table: branches (สาขาทั่วประเทศ)
-- สร้างก่อนเพราะ users อ้างอิง FK มาที่นี่
-- =====================================================

CREATE TABLE branches (
    id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name        VARCHAR(255) NOT NULL,          -- ชื่อสาขา
    region      VARCHAR(100) NOT NULL,          -- ภูมิภาค (เหนือ/กลาง/อีสาน/ใต้)
    address     TEXT,                           -- ที่อยู่เต็ม
    is_active   BOOLEAN DEFAULT true,           -- สถานะเปิด/ปิดสาขา
    created_at  TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- =====================================================
-- Table: users (ผู้ใช้งานระบบ / นักศึกษาครูสมาธิ)
-- =====================================================

CREATE TABLE users (
    id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    line_id         VARCHAR(255) UNIQUE,            -- Line User ID สำหรับ Login
    display_name    VARCHAR(255) NOT NULL,           -- ชื่อที่แสดงในระบบ
    email           VARCHAR(255),                    -- อีเมล (optional)
    phone           VARCHAR(20),                     -- เบอร์โทร (optional, encrypted)
    branch_id       UUID REFERENCES branches(id),    -- สาขาที่สังกัด
    student_status  student_status DEFAULT 'enrolled',
    role            user_role DEFAULT 'student',
    course_level    INTEGER DEFAULT 1,               -- ระดับหลักสูตร (เล่ม 1-3)
    pdpa_consent    BOOLEAN DEFAULT false,           -- ยินยอม PDPA
    pdpa_consent_at TIMESTAMP WITH TIME ZONE,        -- วันที่ยินยอม
    is_active       BOOLEAN DEFAULT true,
    created_at      TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at      TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- =====================================================
-- Table: meditation_logs (บันทึกการปฏิบัติสมาธิ)
-- =====================================================

CREATE TABLE meditation_logs (
    id                UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id           UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    type              meditation_type NOT NULL,       -- นั่งสมาธิ / เดินจงกรม
    duration_minutes  INTEGER NOT NULL CHECK (duration_minutes > 0),  -- จำนวนนาที
    session_date      DATE NOT NULL,                  -- วันที่ปฏิบัติ
    note              TEXT,                            -- บันทึกสภาวะ (optional)
    logged_at         TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- =====================================================
-- Table: ai_feedback (Feedback จากผู้ใช้ต่อคำตอบ AI)
-- =====================================================

CREATE TABLE ai_feedback (
    id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id     UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    question    TEXT NOT NULL,                   -- คำถามที่ถาม
    answer      TEXT NOT NULL,                   -- คำตอบที่ AI ให้
    rating      SMALLINT CHECK (rating IN (1, -1)),  -- 👍 = 1, 👎 = -1
    comment     TEXT,                            -- ความคิดเห็นเพิ่มเติม
    created_at  TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- =====================================================
-- Indexes (สำหรับ Performance)
-- =====================================================

CREATE INDEX idx_users_line_id ON users(line_id);
CREATE INDEX idx_users_branch_id ON users(branch_id);
CREATE INDEX idx_meditation_logs_user_id ON meditation_logs(user_id);
CREATE INDEX idx_meditation_logs_session_date ON meditation_logs(session_date);
CREATE INDEX idx_meditation_logs_user_date ON meditation_logs(user_id, session_date);
CREATE INDEX idx_ai_feedback_user_id ON ai_feedback(user_id);

-- =====================================================
-- Row Level Security (RLS)
-- =====================================================

ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE meditation_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai_feedback ENABLE ROW LEVEL SECURITY;

-- Users: อ่านได้เฉพาะข้อมูลตัวเอง
CREATE POLICY "Users can view own data"
    ON users FOR SELECT
    USING (auth.uid() = id);

CREATE POLICY "Users can update own data"
    ON users FOR UPDATE
    USING (auth.uid() = id);

-- Meditation Logs: จัดการได้เฉพาะ Log ตัวเอง
CREATE POLICY "Users can view own logs"
    ON meditation_logs FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own logs"
    ON meditation_logs FOR INSERT
    WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own logs"
    ON meditation_logs FOR UPDATE
    USING (auth.uid() = user_id);

-- AI Feedback: จัดการได้เฉพาะ Feedback ตัวเอง
CREATE POLICY "Users can view own feedback"
    ON ai_feedback FOR SELECT
    USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own feedback"
    ON ai_feedback FOR INSERT
    WITH CHECK (auth.uid() = user_id);

-- =====================================================
-- Updated_at Trigger (Auto-update timestamp)
-- =====================================================

CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER trigger_branches_updated_at
    BEFORE UPDATE ON branches
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

-- =====================================================
-- Seed Data: ตัวอย่างสาขา
-- =====================================================

INSERT INTO branches (name, region, address) VALUES
    ('สาขา 1 วัดธรรมมงคล', 'กรุงเทพฯ', 'วัดธรรมมงคล เถาบุญนนทวิถี สุขุมวิท 101'),
    ('สาขา 2 วัดสระเกศ', 'กรุงเทพฯ', 'วัดสระเกศราชวรมหาวิหาร แขวงบ้านบาตร เขตป้อมปราบฯ'),
    ('สาขา เชียงใหม่', 'ภาคเหนือ', 'จ.เชียงใหม่'),
    ('สาขา ขอนแก่น', 'ภาคอีสาน', 'จ.ขอนแก่น'),
    ('สาขา สงขลา', 'ภาคใต้', 'จ.สงขลา');
