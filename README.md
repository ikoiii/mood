# Mood and Pain Tracker Web App

Aplikasi web untuk memantau mood dan tingkat nyeri pasien rawat inap secara real-time.

## 🎯 Project Overview

**Backend**: Python FastAPI
**Frontend**: Next.js + Shadcn/UI + Tailwind CSS
**Database**: MySQL (with PyMySQL)
**Authentication**: QR Code Login untuk pasien

## 📋 Sprint 1: Setup Proyek ✅ COMPLETED

### ✅ Selesai:
- [x] Backend FastAPI dengan virtual environment
- [x] Frontend Next.js dengan TypeScript
- [x] Shadcn/UI components setup
- [x] Konfigurasi CORS antara frontend dan backend
- [x] Testing konektivitas API

## 🚀 Quick Start

### 1. Database Setup (XAMPP)

**Required**: XAMPP with MySQL installed

```bash
# 1. Start XAMPP (Apache + MySQL)
# 2. Buat database mood_tracker via phpMyAdmin
# 3. Import SQL script
mysql -u root -p mood_tracker < backend/create_tables.sql
```

**Detailed instructions**: Lihat `DATABASE_SETUP.md`

### 2. Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Akses Aplikasi

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs (Swagger UI)
- **Ping Test**: http://localhost:8000/api/ping

## 📁 Project Structure

```
mood/
├── backend/
│   ├── venv/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── patient.py
│   │   └── entry.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── patients.py
│   │   ├── entries.py
│   │   └── auth.py
│   ├── schemas/
│   ├── services/
│   ├── main.py
│   ├── database.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   ├── lib/
│   │   └── hooks/
│   ├── public/
│   ├── package.json
│   └── components.json
├── claude.md
└── README.md
```

## 🧪 Testing

### Test Backend API
```bash
curl http://localhost:8000/api/ping
# Expected response: {"message": "pong"}
```

### Test Frontend Connection
Buka http://localhost:3000 di browser. Halaman akan menampilkan status koneksi backend.

## 🔄 Next Steps (Sprint 2)

Berikutnya akan dikerjakan:
- CRUD Patients & Entries
- Database models dan schemas
- API endpoints lengkap
- Frontend forms dengan Shadcn/UI

## 🔧 Environment Variables

Copy `.env.example` ke `.env` untuk backend:

```bash
cp backend/.env.example backend/.env
```

Edit file `.env` sesuai konfigurasi database lokal Anda.

## 📝 Notes

- Backend menggunakan PyMySQL sebagai database driver (lebih mudah setup daripada mysqlclient)
- Frontend menggunakan App Router Next.js 15
- Shadcn/UI sudah dikonfigurasi dengan Tailwind CSS
- CORS sudah dikonfigurasi untuk localhost:3000

## 🐛 Troubleshooting

1. **Backend gagal start**: Pastikan Python 3.12+ dan dependencies sudah terinstall
2. **Frontend error**: Jalankan `npm install` ulang
3. **CORS error**: Pastikan backend dan frontend berjalan di port yang benar (8000 dan 3000)
4. **Port conflicts**: Kill semua proses yang berjalan dengan:
   ```bash
   # Kill all development servers
   pkill -f "next dev" && pkill -f "uvicorn"

   # Kill processes using specific ports
   lsof -ti:3000 | xargs -r kill -9
   lsof -ti:8000 | xargs -r kill -9

   # Clean cache
   cd frontend && rm -rf .next
   ```

---

**Sprint 1 Status**: ✅ COMPLETED