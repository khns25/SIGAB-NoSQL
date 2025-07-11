from pymongo import MongoClient
client = MongoClient("mongodb+srv://khaniss250403:TleZ7ozAtL5Hly7K@sigab-cluster.ks4f7o0.mongodb.net/?retryWrites=true&w=majority&appName=SIGAB-Cluster")
db = client["sigab"]
relawan = db["relawan"]

# Query 1: Cari relawan berdasarkan nama
relawan_andi = relawan.find_one({"nama": "Andi Pratama"})
print("\nQuery 1: Data relawan bernama Andi Pratama")
print(relawan_andi)

# Query 2: Cari relawan dengan keahlian medis
relawan_medis = relawan.find({"keahlian": "medis"})
print("\nQuery 2: Relawan dengan keahlian medis")
for r in relawan_medis:
    print(r)

# Query 3: Update status relawan ke non-aktif
result = relawan.update_one(
    {"_id": "relawan_001"},
    {"$set": {"status": "non-aktif"}}
)
print("\nQuery 3: Update status relawan_001 ke non-aktif, modified count:", result.modified_count)

# Query 4: Hapus relawan tertentu
result = relawan.delete_one({"_id": "relawan_001"})
print("\nQuery 4: Menghapus relawan_001, deleted count:", result.deleted_count)

# Query 5: Hitung jumlah relawan aktif
jumlah_aktif = relawan.count_documents({"status": "aktif"})
print("\nQuery 5: Jumlah relawan aktif =", jumlah_aktif)
