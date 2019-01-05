
#name: Phong, Duc, Quan
#salary per hour: 25,25,30
#hours: 20,25,40

# 1/ Tinh luong moi nguoi
# 2/ Tinh tong quy luong

# => nen chay bang list truoc, dict o ben trong

p1 = {
    "name": "Phong",
    "salary": 25,
    "hours": 20

}

d1 = {
    "name": "Duc",
    "salary": 25,
    "hours": 25

}

q1 = {
    "name": "Quan",
    "salary": 30,
    "hours": 40

}

human = [p1,d1,q1]


print("Hi Boss. Our company has 3 staffs, for details:", end=" ")
for v in human:
    print(v["name"], end=" ")

print()
ques = input("Whose salary do you want to know? (P/D/Q): ")

loop = True
while loop:
    if ques == "P" or "p":
        p1_salary = p1["salary"] * p1["hours"]
        print("The salary of", p1["name"], "is: ", p1_salary)
        ques = input("Whose salary do you want to know? (P/D/Q) ")

    elif ques == "D" or "d":
        d1_salary = d1["salary"] * d1["hours"]
        print("The salary of", d1["name"], "is: ", d1_salary)
        ques = input("Whose salary do you want to know? (P/D/Q) ")

    elif ques == "Q" or "q":
        q1_salary = q1["salary"] * q1["hours"]
        print("The salary of", q1["name"], "is: ", q1_salary)
        ques = input("Whose salary do you want to know? (P/D/Q) ")

    else:
        loop = False

print("In below, it 's a salary summary for detail: ")


# p2 = p1["salary"] * p1["hours"]
# print(p2)

x = 0
for i in human:
    n = i["salary"] * i["hours"]
    print(i["name"], n,sep=": ")
    x += n

print("Total salary: ", x)