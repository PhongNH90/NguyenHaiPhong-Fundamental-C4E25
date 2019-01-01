print("Hello my name is Phong and this is my ship size: ")
ship = [4,6,8,2,15,10,6]
print(ship)

m = int(input("Enter month number of producing: "))

for i in range(m):
    print("Month", i+1)
    x = 0
    for j in range(7):
        ship[x] = ship[j] + 50
        x += 1
    print("One month has passed, now it 's my flock: ", ship)
    print("Now my biggest ship has size ", max(ship), "let's shear it")
    ship[ship.index(max(ship))] = 8
    print("After shearing it, here is my flock ")
    print(ship)
    print()

n= sum(ship)
print("My flock has size in total ", n)

revenue = 2 * n
print("Total revenue is: ", revenue, "$")

