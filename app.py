from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # agar bisa diakses dari HTML frontend

# Ganti sesuai URI MongoDB Atlas kamu
client = MongoClient("mongodb+srv://khaniss250403:TleZ7ozAtL5Hly7K@sigab-cluster.ks4f7o0.mongodb.net/?retryWrites=true&w=majority&appName=SIGAB-Cluster")
db = client['sigab']
relawan_col = db['relawan']

@app.route('/api/relawan', methods=['POST'])
def tambah_relawan():
    data = request.json
    relawan_col.insert_one(data)
    return jsonify({"status": "sukses", "pesan": "Relawan ditambahkan"}), 201

@app.route('/api/relawan', methods=['GET'])
def semua_relawan():
    data = list(relawan_col.find({}, {"_id": 0}))
    return jsonify(data)

@app.route('/api/relawan/<nama>', methods=['DELETE'])
def hapus_relawan(nama):
    result = relawan_col.delete_many({"nama": nama})
    if result.deleted_count > 0:
        return jsonify({"status": "sukses", "pesan": "Relawan dihapus"}), 200
    else:
        return jsonify({"status": "gagal", "pesan": "Relawan tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run(debug=True)
