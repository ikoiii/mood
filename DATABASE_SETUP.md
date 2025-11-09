# Database Setup Instructions - XAMPP MySQL

## 📋 Persiapan

Pastikan XAMPP sudah terinstall di sistem Anda. Jika belum, download dari [https://www.apachefriends.org/](https://www.apachefriends.org/)

## 🚀 Langkah 1: Start XAMPP Services

1. Buka XAMPP Control Panel
2. Start Apache dan MySQL services
3. Pastikan kedua service berjalan dengan warna hijau

## 🗄️ Langkah 2: Buat Database melalui phpMyAdmin

### Opsi A: Menggunakan phpMyAdmin (Web Interface)

1. Buka browser dan akses: `http://localhost/phpmyadmin`
2. Klik tab "New" (atau "Databases")
3. Masukkan nama database: `mood_tracker`
4. Pilih collation: `utf8mb4_unicode_ci`
5. Klik "Create"

### Opsi B: Menggunakan Command Line

```bash
# Login ke MySQL
mysql -u root -p

# Buat database
CREATE DATABASE mood_tracker CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Gunakan database
USE mood_tracker;

# Keluar dari MySQL
EXIT;
```

## 📝 Langkah 3: Import SQL Script

### Opsi A: Menggunakan phpMyAdmin

1. Pilih database `mood_tracker` dari sidebar kiri
2. Klik tab "Import"
3. Pilih file `backend/create_tables.sql`
4. Klik "Go" untuk menjalankan script

### Opsi B: Menggunakan Command Line

```bash
# Import file SQL
mysql -u root -p mood_tracker < backend/create_tables.sql
```

## ✅ Langkah 4: Verifikasi Tabel

### Via phpMyAdmin:
- Buka database `mood_tracker`
- Anda akan melihat 2 tabel: `patients` dan `entries`

### Via Command Line:
```sql
mysql -u root -p mood_tracker
SHOW TABLES;
```

Hasil yang diharapkan:
```
+-------------------------+
| Tables_in_mood_tracker  |
+-------------------------+
| entries                 |
| patients                |
+-------------------------+
```

## 🔧 Langkah 5: Konfigurasi Backend

1. Copy file environment:
   ```bash
   cd backend
   cp .env.example .env
   ```

2. Edit file `.env` (jika perlu):
   ```
   DATABASE_URL=mysql+pymysql://root:@localhost/mood_tracker
   ```

3. Install MySQL client library (jika belum):
   ```bash
   source venv/bin/activate
   pip install mysqlclient
   ```

## 🚀 Langkah 6: Test Backend Connection

```bash
cd backend
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Test API endpoint:
```bash
curl http://localhost:8000/api/db-status
```

Expected response:
```json
{"message": "Database connected", "tables_created": true}
```

## 📊 Schema Database

### Tabel: `patients`
- `id` (INT, PRIMARY KEY, AUTO_INCREMENT)
- `name` (VARCHAR(100), NOT NULL)
- `age` (INT, NOT NULL)
- `room` (VARCHAR(20), NOT NULL)
- `qr_token` (VARCHAR(255), UNIQUE, NOT NULL)
- `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

### Tabel: `entries`
- `id` (INT, PRIMARY KEY, AUTO_INCREMENT)
- `patient_id` (INT, FOREIGN KEY → patients.id)
- `mood` (VARCHAR(50), NOT NULL)
- `pain_level` (INT, 0-10, NOT NULL)
- `note` (TEXT, nullable)
- `created_at` (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)

## 📝 Sample Data

SQL script sudah include sample data:
- 3 sample patients
- 3 sample entries

## 🔍 Query Examples

```sql
-- Get all patients
SELECT * FROM patients;

-- Get all entries for patient
SELECT * FROM entries WHERE patient_id = 1;

-- Get latest entry per patient
SELECT p.name, e.mood, e.pain_level, e.created_at
FROM patients p
LEFT JOIN entries e ON p.id = e.patient_id
WHERE e.id = (
    SELECT MAX(id) FROM entries e2 WHERE e2.patient_id = p.id
);

-- Get average pain level per patient
SELECT p.name, AVG(e.pain_level) as avg_pain
FROM patients p
JOIN entries e ON p.id = e.patient_id
GROUP BY p.id;
```

## 🐛 Troubleshooting

### Error: "Can't connect to MySQL server"
- Pastikan MySQL service di XAMPP sudah running
- Cek port 3306 tidak digunakan oleh aplikasi lain

### Error: "Access denied for user 'root'@'localhost'"
- Reset password MySQL root user
- Update DATABASE_URL di .env dengan password yang benar

### Error: "Unknown database 'mood_tracker'"
- Pastikan database sudah dibuat dengan benar
- Cek spelling nama database

### Error: "Table doesn't exist"
- Pastikan SQL script sudah diimport dengan benar
- Cek database yang aktif saat import

## 📂 File Lokasi

- SQL Script: `backend/create_tables.sql`
- Environment Config: `backend/.env.example`
- Database Config: `backend/database.py`

---

**Setelah setup selesai, Anda bisa melanjutkan ke Sprint 3: QR Login Pasien**