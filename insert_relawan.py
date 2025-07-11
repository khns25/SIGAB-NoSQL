from pymongo import MongoClient

# Koneksi ke MongoDB Atlas
client = MongoClient("mongodb+srv://khaniss250403:TleZ7ozAtL5Hly7K@sigab-cluster.ks4f7o0.mongodb.net/?retryWrites=true&w=majority&appName=SIGAB-Cluster")

# Pilih database dan koleksi
db = client["sigab"]
relawan = db["relawan"]

data1 = {
    "nama": "kasya",
    "keahlian": ["medis"],
    "lokasi": "makassar",
    "status": "aktif",
    "aktivitas": "palu-evakuasi korban"
}

data2 = {
    "nama": "andika",
    "keahlian": ["logistik"],
    "lokasi": "Makassar",
    "status": "aktif",
    "aktivitas": "Palu - Distribusi makanan"
}

data3 = {
    "nama": "nisa",
    "keahlian": ["logistik"],
    "lokasi": "kendari",
    "status": "aktif",
    "aktivitas": "makassar-distribusi makanan"
}

relawan.insert_one(data1)
relawan.insert_one(data2)
relawan.insert_one(data3)
print("Data relawan berhasil disimpan!")