from pymongo import MongoClient
uri = "mongodb://admin:admin1@ds055802.mlab.com:55802/c4e25"

#Bước 1: Kết nối đến mLab
client = MongoClient(uri)

#Bước 2: Get a database
db = client.get_database()

#Bước 3: get a collection (mở tủ)
post_collection = db["posts"]

#Bước 4: Create a document
new_post = {
    "title": "Đang suy nghĩ",              #field title
    "content": "Tối ăn lẩu bò hay lẩu gà"   #field content
}


#Lazy loading
post_list = post_collection.find()          #cursor ( Con trỏ, trỏ đến nơi nào cần)
first_post = post_list[0]
print(first_post)           #đọc chi tiết từng file trong tủ

for p in post_list:         #đọc xem trong tủ có những gì
    print(p)


#Bước 5: Insert a document
# post_collection.insert_one(new_post)

#Bước 6: Close connection
client.close()
