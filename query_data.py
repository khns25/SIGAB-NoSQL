from pymongo import MongoClient

client = MongoClient("mongodb+srv://khaniss250403:TleZ7ozAtL5Hly7K@sigab-cluster.ks4f7o0.mongodb.net/?retryWrites=true&w=majority&appName=SIGAB-Cluster")
db = client["sigab"]
relawan = db["relawan"]

# 1. Mencari relawan berdasarkan nama
relawan_kasya = relawan.find_one({"nama": "kasya"})
print("\nQuery 1: Data relawan bernama kasya")
if relawan_kasya:
    print(relawan_kasya)
else:
    print("Tidak ditemukan.")

# 2. Menemukan relawan berdasarkan keahlian
relawan_logistik = relawan.find({"keahlian": "logistik"})
print("\nQuery 2: Relawan dengan keahlian logistik")
for r in relawan_logistik:
    print(r)

# 3. Memperbarui status relawan (misal: nisa jadi non-aktif)
result = relawan.update_one(
    {"nama": "nisa"},
    {"$set": {"status": "non-aktif"}}
)
print("\nQuery 3: Update status nisa ke non-aktif, modified count:", result.modified_count)

# 4. Menghapus data relawan (misal: andika)
result = relawan.delete_one({"nama": "andika"})
print("\nQuery 4: Menghapus relawan andika, deleted count:", result.deleted_count)

# 5. Menghitung jumlah relawan aktif
jumlah_aktif = relawan.count_documents({"status": "aktif"})
print("\nQuery 5: Jumlah relawan aktif =", jumlah_aktif)