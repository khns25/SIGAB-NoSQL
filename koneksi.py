from pymongo import MongoClient

client = MongoClient("mongodb+srv://khaniss250403:TleZ7ozAtL5Hly7K@sigab-cluster.ks4f7o0.mongodb.net/?retryWrites=true&w=majority&appName=SIGAB-Cluster")

db = client["sigab"]
relawan = db["relawan"]
