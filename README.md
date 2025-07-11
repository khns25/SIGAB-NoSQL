# SIGAB - NoSQL Project

Repositori ini berisi kode sumber tugas besar NoSQL pada studi kasus **Sistem SIGAB**: Aplikasi Pencatatan Aktivitas Relawan Bencana.

## 📦 Kode Sumber

- `app.py`: Backend Flask dengan REST API untuk operasi CRUD relawan
- `insert_relawan.py`: Script Python untuk koneksi ke MongoDB Atlas dan memasukkan data relawan ke dalam koleksi
- `query_data.py`: Script Python berisi minimal 5 query MongoDB yang relevan untuk kebutuhan sistem
- `show_relawan.py`: Script untuk menampilkan semua data relawan dari database
- `koneksi.py`: File konfigurasi koneksi MongoDB Atlas
- `index.html`: Antarmuka web dengan integrasi langsung ke backend API

## ⚙️ Setup Lingkungan

1. Pastikan Python 3.8 atau lebih tinggi sudah terinstal
2. Install dependencies:
   ```bash
   pip install pymongo flask flask-cors
   ```
3. Buat akun dan cluster MongoDB Atlas di [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
4. Whitelist IP perangkat dan salin connection string
5. Ubah URI koneksi di semua file Python sesuai connection string MongoDB Atlas

## 🚀 Cara Menjalankan

1. **Jalankan Flask Backend:**
   ```bash
   python app.py
   ```
   Server akan berjalan di `http://localhost:5000`

2. **Jalankan script Python (opsional):**
   - `python insert_relawan.py` - Tambah data relawan
   - `python query_data.py` - Jalankan query MongoDB
   - `python show_relawan.py` - Tampilkan semua data

3. **Akses Web Interface:**
   - Buka `index.html` di browser (disarankan via Live Server)
   - Interface sudah terintegrasi dengan backend API

## 🔌 API Endpoints

- `POST /api/relawan` - Tambah relawan baru
- `GET /api/relawan` - Ambil semua data relawan
- `DELETE /api/relawan/<nama>` - Hapus relawan berdasarkan nama

## 🗂️ Struktur Database

- **Database**: `sigab`
- **Collection**: `relawan`
- Struktur dokumen menggunakan format JSON dengan embedded field untuk aktivitas relawan

## 📊 Query MongoDB yang Tersedia

Script `query_data.py` berisi 5 query utama:
1. Mencari relawan berdasarkan nama
2. Menemukan relawan berdasarkan keahlian
3. Memperbarui status relawan
4. Menghapus data relawan
5. Menghitung jumlah relawan aktif

## 🧾 Keterangan Tambahan

- Sistem menggunakan pendekatan document-oriented (MongoDB)
- Antarmuka web sudah terintegrasi langsung dengan database melalui Flask REST API
- Data dapat diverifikasi melalui MongoDB Compass atau script Python
- Menggunakan CORS untuk mengizinkan akses dari frontend HTML
- Frontend menggunakan Bootstrap untuk tampilan yang responsif

## 🔧 Fitur yang Tersedia

- ✅ Tambah data relawan melalui form web
- ✅ Tampilkan data relawan dalam bentuk kartu
- ✅ Hapus data relawan berdasarkan nama
- ✅ Query data menggunakan script Python
- ✅ Integrasi real-time antara frontend dan backend
