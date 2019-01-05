tudien = ["eny", "any", "stt", "lm", "ngta", "shmily"]

tudien = {
    "eny": "Em nguoi yeu",
    "any": "Anh nguoi yeu",
    "stt": "status",
    "lm": "lam",
    "ngta": "nguoi ta",
    "shmily": "see how much i love you",

}

# del tudien["eny"]
# del tudien[0]         #xoa mot phan tu
# print(tudien)

# menu = [1,2,3]    
# del menu[0]        #xoa mot phan tu trong list


# n = input("Code: ")

# loop = True
# while loop:
#     if n not in tudien:
#         print("Sorry, Code again: ")
#         n = input("Code: ")
#     else:
#         loop = False

# print("Translation:", tudien[n])              #không thể nào in ra vị trí của tudien[0]

tudien["eny"] = "Anh nguoi yeu" #update
tudien["love"] = 2  #create, insert

print(tudien)

# print(tudien["skills"])       #error


if "skills" in tudien:  #kiem tra xem mot phan tu co nam trong list/dictionary hay khong?
    print("OK")

else:
    print("Not OK")







