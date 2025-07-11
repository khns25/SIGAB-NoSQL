from pymongo import MongoClient

client = MongoClient("mongodb+srv://khaniss250403:TleZ7ozAtL5Hly7K@sigab-cluster.ks4f7o0.mongodb.net/?retryWrites=true&w=majority&appName=SIGAB-Cluster")
db = client["sigab"]
relawan = db["relawan"]

results = relawan.find()

print("\n=== Daftar Data Relawan di Database SIGAB ===")
for r in results:
    print(f"ID        : {r.get('_id', '-')}")
    print(f"Nama      : {r.get('nama', '-')}")
    print(f"Keahlian  : {', '.join(r.get('keahlian', []))}")
    print(f"Lokasi    : {r.get('lokasi', '-')}")
    print(f"Status    : {r.get('status', '-')}")
    print(f"Aktivitas : {r.get('aktivitas', '-')}")
    print("-" * 40)