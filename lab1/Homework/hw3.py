from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#Bước 1: Kết nối đến mLab
client = MongoClient(uri)

#Bước 2: Get a database
db = client.get_database()

#Bước 3: get a collection (mở tủ)
post_collection = db["posts"]

#Bước 4: Create a document
new_post = {
    "title": "C4E25",
    "author": "Nguyen Hai Phong",
    "content": "Chúc mừng năm mới Tất cả Anh chị em. Chúc Anh em luôn Mạnh khỏe, Hạnh phúc & Bình an. Thanks Techkids!!"
}

#Bước 5: Insert a document
post_collection.insert_one(new_post)

client.close()