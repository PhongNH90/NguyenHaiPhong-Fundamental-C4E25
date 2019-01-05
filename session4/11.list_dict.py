p1 = {
    "name": "phong",
    "age": 28

}

p2 = {
    "name": "ha",                   #giong keys   #du lieu dong dang
    "age": 28

}


p3 = {
    "name": "lam",                   
    "age": 3

}


p_list = []

# print(p_list)

# p_list.append(p1)               #insert dict trong list
# # print(p_list)

# p_list.append(p2)
# p_list.append(p3)
# # print(p_list)

# p_first = p_list[0]
# print(p_first)

# # print(p_first["name"])

p_list = [p1,p2,p3]         #cho các dict vào trong list

for p in p_list:                        #in tất cả phần tử đồng chất trong list
    print(p["name"], p["age"])



#cach thuc bo cuc du lieu quan trong hon la tinh logic

