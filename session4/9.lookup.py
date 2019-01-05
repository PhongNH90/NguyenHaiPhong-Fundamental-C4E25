tudien = {
    "eny": "Em nguoi yeu",
    "any": "Anh nguoi yeu",
    "stt": "status",
    "lm": "lam",
    "ngta": "nguoi ta",
    "shmily": "see how much i love you",

}

# tudien["eny"] = "Anh nguoi yeu"
# print(tudien)

n = input("Code: ")

loop = True
while loop:
    if n not in tudien:
        print("Sorry, not exist")
        dictnew = input("please add new word you want (Y/N)? ").upper()
        if dictnew == "Y":
            enter = input("Enter new translation: ")
            tudien[n] = enter
            print(tudien)
        else:
            n = input("Code: ")
    else:
        loop = False
        print("Translation:", tudien[n])


# print(tudien)


# while True:
#     m = input("Do you want to update (Y/N)? ")
#     print(m)

#     if m == "Y" or "y":
#         i = input("Enter new translation: ")
#         print(i)
#         tudien[n] = i

#     print(tudien)

