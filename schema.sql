-- ShootPlan Database Schema for Supabase

-- Foydalanuvchilar (Users) jadvali
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(50) DEFAULT 'admin',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Mijozlar (Clients) jadvali
CREATE TABLE IF NOT EXISTS clients (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(255) NOT NULL,
    phone VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Syomkalar (Shoots) jadvali
CREATE TABLE IF NOT EXISTS shoots (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    client_id UUID REFERENCES clients(id) ON DELETE CASCADE,
    shoot_date TIMESTAMP WITH TIME ZONE NOT NULL,
    type VARCHAR(100), -- Masalan: wedding, portrait, commercial, video
    status VARCHAR(50) DEFAULT 'pending', -- pending, confirmed, completed
    location VARCHAR(255),
    price VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Row Level Security (RLS) qoidalarini yoqish (agar to'g'ridan-to'g'ri frontenddan ulasangiz kerak bo'ladi)
-- ALTER TABLE users ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE clients ENABLE ROW LEVEL SECURITY;
-- ALTER TABLE shoots ENABLE ROW LEVEL SECURITY;

-- Ilova foydalanuvchilari (App Users) jadvali (Authentication uchun)
CREATE TABLE IF NOT EXISTS app_users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    approval_status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
