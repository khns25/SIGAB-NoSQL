from pymongo import MongoClient

# Koneksi ke MongoDB Atlas
client = MongoClient("mongodb+srv://khaniss250403:TleZ7ozAtL5Hly7K@sigab-cluster.ks4f7o0.mongodb.net/?retryWrites=true&w=majority&appName=SIGAB-Cluster")

# Pilih database dan koleksi
db = client["sigab"]
relawan = db["relawan"]

# Data dummy relawan
data = {
    "_id": "relawan_001",
    "nama": "Andi Pratama",
    "keahlian": ["medis", "logistik"],
    "lokasi_domisili": "Makassar",
    "kontak": {
        "telepon": "08123456789",
        "email": "andi.pratama@mail.com"
    },
    "status": "aktif",
    "aktivitas": [
        {
            "id_aktivitas": "akt_1001",
            "lokasi": "Palu",
            "tanggal": "2025-06-01",
            "deskripsi": "Distribusi makanan"
        }
    ]
}

# Insert data ke MongoDB
relawan.insert_one(data)
print("Data relawan berhasil disimpan!")
