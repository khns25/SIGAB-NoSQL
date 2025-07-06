# SIGAB - NoSQL Project

Repositori ini berisi kode sumber tugas besar NoSQL pada studi kasus Sistem SIGAB: Aplikasi Pencatatan Aktivitas Relawan Bencana.

## 📦 Kode Sumber
- insert_data.py: Script untuk koneksi ke MongoDB dan memasukkan data relawan.
- query_data.py: Script berisi minimal 5 query yang relevan untuk kebutuhan sistem SIGAB.

## ⚙️ Setup Lingkungan
1. Pastikan Python 3.8+ sudah terinstal.
2. Install pymongo: !pip install pymongo
3. Buat database MongoDB Atlas, whitelist IP, dan ambil connection string.
4. Ubah string koneksi di script sesuai database kamu.

## 📚 Cara Menjalankan
- Jalankan `insert_data.py` untuk memasukkan data.
- Jalankan `query_data.py` untuk menjalankan query.

## 🗂️ Database
- Menggunakan MongoDB Atlas sebagai database NoSQL.
- Database: sigab
- Koleksi: relawan

