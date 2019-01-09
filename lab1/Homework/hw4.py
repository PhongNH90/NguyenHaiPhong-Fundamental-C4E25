from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#Bước 1: Kết nối đến mLab
client = MongoClient(uri)

#Bước 2: Get a database
db = client.get_database()

#Bước 3: get a collection (mở tủ)
cus_collection = db["customers"]

#Lazy loading
cus_list = cus_collection.find()         

events_sum = 0
wom_sum = 0
ads_sum = 0

for i in cus_list:
    if i["ref"] == "events":
        events_sum += 1
        
    elif i["ref"] == "wom":
        wom_sum += 1
       
    elif i["ref"] == "ads":
        ads_sum += 1
        
    
print("Total number of events group: ", events_sum)
print("Total number of wom group: ", wom_sum)
print("Total number of ads group: ", ads_sum)


from matplotlib import pyplot

person_count = [3902, 1132, 1938]
person_group = ["events", "wom", "ads"]

pyplot.pie(person_count, labels=person_group, autopct="%.1f%%", shadow=True, explode=[0, 0.2, 0])
pyplot.title("Percentage of Each Group")

pyplot.axis("equal")

pyplot.show()


