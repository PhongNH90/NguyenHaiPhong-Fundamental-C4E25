print("Hello my name is Phong and this is my ship size: ")
ship = [4,6,8,2,15,10,6]
print(ship)

# ship.sort()
print("Now my biggest ship has size ", max(ship), "let's shear it")

ship[4] = 8
print("After shearing it, here is my flock ")
print(ship)

ship_inc = [x+50 for x in ship]
print("One month has passed, now it 's my flock: ", ship_inc)