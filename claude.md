### **🧠 *Product Requirements Document (PRD)***

#### **Project: Mood and Pain Tracker Web App**

#### **Stack:**

* **Frontend:** Next.js \+ Shadcn/UI \+ Tailwind CSS  
* **Backend:** Python FastAPI  
* **Database:** MySQL/XAMPP  
* **Authentication:** QR Code Login untuk pasien  
* **Hosting:** Vercel (frontend), Render/Railway (backend)

---

### **1\. 🎯 *Latar Belakang & Tujuan***

Perawat dan dokter sering kesulitan memantau kondisi emosional dan tingkat nyeri pasien rawat inap secara berkala. Aplikasi *Mood and Pain Tracker* bertujuan untuk mempermudah pasien dalam melaporkan suasana hati (mood) dan tingkat nyeri (pain level), serta membantu tenaga medis memantau perkembangan pasien secara real-time melalui dashboard visual.  
**Tujuan Utama:**

* Memfasilitasi *input mood dan pain level* pasien secara cepat melalui antarmuka yang sederhana.  
* Menyediakan *dashboard real-time* untuk memantau kondisi pasien.  
* Mempermudah *pengelolaan data pasien* dengan fitur CRUD.  
* Mendukung *login pasien via QR Code* agar mudah digunakan di lingkungan rumah sakit.

---

### **2\. 🎯 *Sasaran Pengguna***

| Tipe Pengguna | Deskripsi | Tujuan Penggunaan |
| :---- | :---- | :---- |
| **Pasien** | Pengguna yang sedang dirawat | Menginput mood & pain level melalui QR login |
| **Perawat** | Tenaga medis pemantau pasien | Melihat dashboard & menganalisis grafik perubahan pasien |
| **Dokter** | Tenaga medis pengambil keputusan | Melihat data dan menentukan intervensi medis |
| **Admin Sistem** | Operator aplikasi | Mengelola data pasien dan riwayat entri |

---

### **3\. 🧩 *Fitur Utama***

#### **A. *Login Pasien (QR Code)***

* Pasien login dengan *memindai QR Code unik* yang berisi ID/token pasien.  
* QR Code dapat dihasilkan oleh admin/perawat.  
* Setelah login, pasien diarahkan ke halaman input mood & pain level.

#### **B. *Input Mood dan Pain Level***

* Mood diinput melalui \*ikon emosi (🙂 😐 😞 😡 😭).  
* Pain level berupa **slider 0–10** (0 \= tidak sakit, 10 \= sangat sakit).  
* Opsional: kolom catatan (“note”) untuk menambahkan deskripsi singkat.  
* Setelah dikirim, data disimpan di tabel entries.

#### **C. *Dashboard Real-time***

* Untuk *perawat/dokter* menampilkan:  
  * Grafik perubahan mood dan pain level per pasien (real-time).  
  * Filter berdasarkan waktu (hari ini, minggu ini, semua waktu).  
  * Daftar pasien aktif dengan status terakhir.  
* Menggunakan *WebSocket* untuk update grafik secara langsung.

#### **D. *CRUD Data Pasien & Entri***

* **Create:** Tambah pasien baru (nama, umur, kamar).  
* **Read:** Lihat daftar pasien dan entri mereka.  
* **Update:** Edit informasi pasien / entri yang salah.  
* **Delete:** Hapus pasien / entri (dengan konfirmasi).

---

### **4\. 🧱 *Struktur Database***

#### ***Tabel: patients***

| Field | Tipe Data | Keterangan |
| :---- | :---- | :---- |
| id | INT (PK, Auto Increment) | ID unik pasien |
| name | VARCHAR(100) | Nama pasien |
| age | INT | Umur pasien |
| room | VARCHAR(20) | Nomor kamar |
| qr\_token | VARCHAR(255) | Token unik login QR (Unique) |
| created\_at | TIMESTAMP | Waktu pendaftaran |

#### ***Tabel: entries***

| Field | Tipe Data | Keterangan |
| :---- | :---- | :---- |
| id | INT (PK, Auto Increment) | ID entri |
| patient\_id | INT (FK → patients.id) | ID pasien |
| mood | VARCHAR(50) | Mood (happy, sad, angry, neutral, etc.) |
| pain\_level | INT | Skala 0–10 |
| note | TEXT | Catatan opsional |
| created\_at | TIMESTAMP | Waktu entri dibuat |

---

### **5\. ⚙️ *Arsitektur Sistem***

Frontend (Next.js \+ Shadcn/UI)  
    │  
    ├── REST API / WebSocket  
    │  
Backend (FastAPI)  
    ├── Auth Controller (QR Login, JWT Admin)  
    ├── Patient Controller (CRUD)  
    ├── Entry Controller (CRUD \+ real-time updates)  
    ├── Database ORM (SQLAlchemy)  
    │  
Database (MySQL / PostgreSQL)

---

### **6\. 🧑‍💻 *Desain Alur Pengguna***

#### **🧍‍♂️ Pasien:**

1. Scan QR → otomatis login ke /patient/{qr\_token}.  
2. Aplikasi memvalidasi token, lalu mengarahkan ke halaman input.  
3. Pilih mood & geser slider pain level.  
4. Kirim data → tampil notifikasi “Data berhasil dikirim”.  
5. Sesi berakhir (logout otomatis) setelah 10 menit.

#### **🧑‍⚕️ Perawat/Dokter (Admin Role):**

1. Login melalui halaman /login (email/password).  
2. Menerima JWT Token.  
3. Masuk ke /dashboard → lihat daftar pasien.  
4. Klik salah satu pasien → lihat grafik mood & pain level.  
5. Pergi ke /admin/patients → Tambah/Edit/Hapus data pasien \+ Generate QR Code.

---

### **7\. 🎨 *Desain UI (Shadcn/UI Components)***

| Halaman | Komponen Shadcn yang digunakan |
| :---- | :---- |
| Login Admin | \<Card\>, \<Input\>, \<Button\>, \<Label\> |
| Input Mood | \<Card\>, \<ToggleGroup\> (untuk ikon mood), \<Slider\>, \<Textarea\>, \<Button\> |
| Dashboard | \<Card\>, \<Chart\> (via Recharts), \<Table\>, \<Select\> (filter) |
| CRUD Pasien | \<Dialog\>, \<Form\>, \<DataTable\>, \<Button\> (utk generate QR) |
| Navigasi | \<Menubar\>, \<Sidebar\> (jika perlu), \<Avatar\> |

Shadcn/UI memberikan gaya profesional dan integrasi mudah dengan Tailwind.  
---

### **8\. 🔐 *Keamanan & Autentikasi***

* **Pasien:** Login via qr\_token yang unik dan *short-lived* (atau divalidasi di backend). Tidak ada password.  
* **Admin/Dokter/Perawat:** Login via JWT Auth (email \+ password).  
* Semua endpoint API admin dilindungi dengan *CORS \+ JWT Bearer Token*.  
* Validasi input (mood, pain\_level, dsb) menggunakan *Pydantic schema* di FastAPI.

---

### **9\. 📊 *Integrasi Dashboard Real-time***

* Backend FastAPI menyediakan endpoint *WebSocket* di /ws/dashboard.  
* Saat entri baru dibuat (via POST ke /entries), *Entry Controller* akan mem-broadcast data baru ke semua koneksi WebSocket yang aktif.  
* Frontend Next.js (di halaman Dashboard) menggunakan *React hooks* (misal: use-socket-io atau *native WebSocket*) untuk terhubung dan me-render ulang data.  
* Data grafik di-render dengan **Recharts**:  
  * Line chart: Pain level vs Time.  
  * Area chart / bar chart: Distribusi mood harian.

---

### **10\. 🧪 *Testing & Validasi***

| Jenis Pengujian | Tools | Deskripsi |
| :---- | :---- | :---- |
| Unit Test | Pytest | Menguji *business logic* di *controllers* backend. |
| Integration Test | Postman / Pytest | Uji API FastAPI ↔ Database (SQLAlchemy). |
| UI Test | Playwright | Uji alur login (Admin & QR) dan input frontend. |
| Load Test | Locust | Uji kestabilan dashboard real-time (WebSocket). |

---

### **11\. 🚀 *Rencana Pengembangan (MVP – Final)***

| Tahap | Fitur Utama | Estimasi |
| :---- | :---- | :---- |
| **Sprint 1** | Setup proyek Next.js \+ FastAPI \+ DB | 3 hari |
| **Sprint 2** | CRUD pasien & entries | 5 hari |
| **Sprint 3** | QR login pasien | 3 hari |
| **Sprint 4** | Dashboard real-time (WebSocket) | 4 hari |
| **Sprint 5** | UI Polishing (Shadcn) \+ Testing | 3 hari |
| **Sprint 6** | Deployment (Vercel \+ Render) | 2 hari |

---

### **12\. 📁 *Struktur Folder (Usulan)***

#### **Frontend (Next.js)**

/frontend  
 ├─ /app  
 │   ├─ page.tsx             (Halaman landing/login admin)  
 │   ├─ /patient  
 │   │  ├─ /\[token\]/page.tsx (Halaman input mood/pain)  
 │   ├─ /dashboard  
 │   │  ├─ page.tsx  
 │   ├─ /admin  
 │   │  ├─ /patients/page.tsx (CRUD Pasien)  
 ├─ /components (Shadcn UI)  
 ├─ /lib (utils, api.ts)  
 └─ /hooks (useWebSocket.ts)

#### **Backend (FastAPI)**

/backend  
 ├─ main.py  
 ├─ /routers  
 │   ├─ patients.py  
 │   ├─ entries.py  
 │   └─ auth.py  
 ├─ /models  
 │   ├─ patient.py  
 │   └─ entry.py  
 ├─ /schemas (Pydantic models)  
 ├─ /services  
 │   ├─ qr\_service.py  
 │   └─ websocket\_service.py  
 ├─ database.py  
 └─ requirements.txt

---

### **13\. 🧾 *Deliverables***

* Dokumentasi API (Otomatis via Swagger UI / ReDoc FastAPI).  
* File .env.example untuk backend & frontend.  
* Script SQL (jika tidak menggunakan auto-migrate) untuk pembuatan tabel.  
* Panduan setup & run proyek lokal (di README.md).

---

### **14\. 📈 *Rencana Pengembangan Lanjutan***

* Notifikasi *push/email* ke perawat jika pain\_level \> 7\.  
* AI-assisted analysis: deteksi tren mood menurun.  
* Export laporan pasien (PDF/Excel).  
* Integrasi login SSO rumah sakit (untuk Admin/Dokter).

---

### **15\. ⚠️ *Non-Functional Requirements (NFR)* (Tambahan)**

* **Performance:** Halaman dashboard (termasuk grafik) harus *load* dalam \< 3 detik. Input pasien harus terkirim dalam \< 1 detik.  
* **Reliability:** Uptime sistem 99.9%.  
* **Usability:** Aplikasi harus *responsive* dan dapat digunakan dengan mudah di tablet (yang biasa dibawa perawat/pasien).  
* **Scalability:** Sistem harus mampu menangani 100 pasien yang menginput data secara bersamaan dan 20 perawat yang memantau dashboard secara konkuren.  
* **Data Security:** Data pasien (HIPAA/Data Privasi) harus dienkripsi saat transit (HTTPS/WSS) dan *at-rest* (jika memungkinkan di database).

---

## **2\. 📚 Panduan Tutorial Pengembangan (Awal Hingga Akhir)**

Berikut adalah panduan *high-level* berdasarkan 6 sprint yang telah Anda tentukan.

### **Sprint 1: Setup Proyek (3 Hari)**

**Tujuan:** Memastikan *stack* frontend, backend, dan database dapat berkomunikasi.

1. **Backend (FastAPI):**  
   * Buat folder /backend.  
   * Setup *virtual environment* (python \-m venv venv).  
   * Install library: pip install fastapi uvicorn sqlalchemy mysqlclient pydantic.  
   * Buat main.py: Setup aplikasi FastAPI dasar.  
   * Buat database.py: Konfigurasi SQLAlchemy *engine* untuk terhubung ke MySQL/XAMPP Anda.  
   * Buat file .env untuk menyimpan kredensial database.  
   * Jalankan server: uvicorn main:app \--reload.  
2. **Frontend (Next.js):**  
   * Buat folder /frontend.  
   * Jalankan npx create-next-app@latest. Pilih TypeScript & App Router.  
   * Install Shadcn/UI: npx shadcn-ui@latest init.  
   * Buat halaman *dummy* (/app/page.tsx).  
3. **Konektivitas:**  
   * Di main.py, buat endpoint T-shirt: @app.get("/api/ping") yang mengembalikan {"message": "pong"}.  
   * Di page.tsx (Next.js), gunakan useEffect dan fetch untuk memanggil /api/ping dan tampilkan pesannya.  
   * **Penting:** Konfigurasi CORS di FastAPI (CORSMiddleware) agar Next.js (dari localhost:3000) diizinkan mengakses FastAPI (di localhost:8000).

---

### **Sprint 2: CRUD Pasien & Entries (5 Hari)**

**Tujuan:** Membangun inti fungsionalitas aplikasi (mengelola data).

1. **Backend (FastAPI):**  
   * **Models:** Buat models/patient.py dan models/entry.py menggunakan *declarative base* SQLAlchemy.  
   * **Schemas:** Buat file *schema* Pydantic untuk validasi data (misal: PatientCreate, PatientRead, EntryCreate).  
   * **Routers:**  
     * Buat routers/patients.py. Implementasikan endpoint /patients/ (GET, POST) dan /patients/{id} (GET, PUT, DELETE).  
     * Buat routers/entries.py. Implementasikan endpoint serupa.  
   * **Test:** Gunakan http://localhost:8000/docs (Swagger UI) untuk menguji semua endpoint CRUD Anda secara manual.  
2. **Frontend (Next.js):**  
   * Buat lib/api.ts: Tempatkan semua fungsi fetch (GET, POST, PUT, DELETE) di sini.  
   * Buat halaman /admin/patients.  
   * Gunakan komponen Shadcn \<DataTable\> untuk menampilkan daftar pasien.  
   * Gunakan Shadcn \<Dialog\> yang berisi \<Form\> untuk *Create* dan *Update* pasien.  
   * Implementasikan *server actions* atau *client-side logic* untuk memanggil api.ts saat form disubmit.

---

### **Sprint 3: QR Login Pasien (3 Hari)**

**Tujuan:** Menerapkan alur login unik untuk pasien tanpa password.

1. **Backend (FastAPI):**  
   * Update models/patient.py: Tambahkan field qr\_token: str (pastikan unik).  
   * Buat services/qr\_service.py: Buat fungsi generate\_unique\_token().  
   * Update routers/patients.py: Saat membuat pasien baru (POST) atau me-request QR (mungkin endpoint baru POST /patients/{id}/generate-qr), panggil qr\_service untuk membuat token dan menyimpannya ke database.  
   * Buat routers/auth.py:  
     * Buat endpoint GET /auth/patient/{token}.  
     * Fungsi ini akan mencari pasien berdasarkan qr\_token. Jika ketemu, kembalikan data pasien (atau JWT khusus pasien jika perlu). Jika tidak, kembalikan 404\.  
2. **Frontend (Next.js):**  
   * **Admin Side:** Di halaman /admin/patients, tambahkan tombol "Generate QR" di setiap baris tabel. Saat diklik, panggil endpoint POST /patients/{id}/generate-qr.  
   * Gunakan library qrcode.react untuk menampilkan qr\_token (atau URL lengkap, misal: https://app.com/patient/{token}) sebagai gambar QR.  
   * **Patient Side:** Buat halaman /patient/\[token\]/page.tsx.  
     * Di halaman ini, ambil token dari URL.  
     * Panggil GET /auth/patient/{token} untuk memvalidasi.  
     * Jika valid, tampilkan halaman input (Gunakan Shadcn \<ToggleGroup\> untuk ikon mood, \<Slider\> untuk pain, \<Textarea\> untuk note).  
     * Jika tidak valid, tampilkan pesan error.

---

### **Sprint 4: Dashboard Real-time (4 Hari)**

**Tujuan:** Menampilkan data secara *live* menggunakan WebSocket.

1. **Backend (FastAPI):**  
   * Install pip install websockets.  
   * Buat services/websocket\_service.py: Buat ConnectionManager *class* untuk mengelola koneksi (menyimpan, menghapus, dan *broadcast* pesan).  
   * Di main.py, buat *global instance* manager \= ConnectionManager().  
   * Buat endpoint WebSocket: @app.websocket("/ws/dashboard"). Fungsi ini akan await manager.connect(websocket) dan menunggunya disconnect.  
   * Update routers/entries.py: Setelah entri baru berhasil disimpan (di dalam fungsi POST), panggil await manager.broadcast(new\_entry\_data).  
2. **Frontend (Next.js):**  
   * Buat halaman /dashboard/page.tsx.  
   * Gunakan *custom hook* (useWebSocket) atau library (socket.io-client jika backend pakai Socket.IO, atau *native WebSocket*).  
   * useEffect untuk terhubung ke ws://localhost:8000/ws/dashboard.  
   * Simpan data pasien/entri di *React state* (misal useState).  
   * Saat menerima pesan baru dari WebSocket, update *state* tersebut.  
   * Install recharts.  
   * Masukkan komponen \<LineChart\> dan \<BarChart\> (dari Recharts), dan berikan *state* Anda sebagai *props* data. Grafik akan otomatis ter-update saat *state* berubah.

---

### **Sprint 5: UI Polishing (Shadcn) \+ Testing (3 Hari)**

**Tujuan:** Mempercantik tampilan dan memastikan aplikasi bebas *bug*.

1. **UI Polishing (Frontend):**  
   * Tinjau semua halaman (Login Admin, Dashboard, CRUD Admin, Input Pasien).  
   * Pastikan konsistensi *spacing*, *font*, dan penggunaan komponen Shadcn.  
   * Tambahkan *loading state* (menggunakan Shadcn \<Skeleton\>) saat data diambil.  
   * Tambahkan notifikasi (menggunakan Shadcn \<Toast\>) untuk aksi (misal: "Data berhasil dikirim").  
   * Pastikan aplikasi *responsive* di tablet menggunakan *utility class* Tailwind (misal: md:, lg:).  
2. **Testing (Backend):**  
   * Install pip install pytest httpx.  
   * Buat folder /tests.  
   * Gunakan TestClient dari FastAPI untuk menguji *unit test* setiap endpoint (misal: test\_create\_patient\_success, test\_create\_patient\_invalid\_data).  
3. **Testing (Frontend/E2E):**  
   * Install Playwright: npx playwright test.  
   * Buat *test script* untuk alur utama:  
     1. Admin login.  
     2. Admin membuat pasien baru.  
     3. Admin melihat QR.  
     4. (Simulasikan) Pasien mengunjungi URL QR.  
     5. Pasien mengirimkan data mood/pain.  
     6. Admin melihat data baru tersebut di dashboard (secara real-time).

---

### **Sprint 6: Deployment (2 Hari)**

**Tujuan:** Membuat aplikasi dapat diakses secara *online*.

1. **Backend (Render):**  
   * Buat file requirements.txt (pip freeze \> requirements.txt).  
   * Pastikan *Start Command* di Render di-set ke: uvicorn main:app \--host 0.0.0.0 \--port $PORT.  
   * Buat database MySQL baru di layanan *cloud* (seperti PlanetScale, Aiven, atau Railway) dan hubungkan ke XAMPP lokal Anda jika perlu *copy* data.  
   * Set *Environment Variables* di Render: DATABASE\_URL, JWT\_SECRET\_KEY, dll.  
2. **Frontend (Vercel):**  
   * Pastikan proyek Next.js Anda ada di repositori GitHub/GitLab.  
   * Hubungkan repositori tersebut ke Vercel (prosesnya otomatis).  
   * Set *Environment Variable* di Vercel: NEXT\_PUBLIC\_API\_URL (isi dengan URL backend Render Anda).  
   * *Push* ke *branch* main, dan Vercel akan otomatis men-deploy.  
3. **Final Test:** Buka URL Vercel Anda dan uji fungsionalitasnya secara menyeluruh.

