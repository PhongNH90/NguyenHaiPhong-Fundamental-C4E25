# def is_inside(a,b):
#     check = True
#     if a[0] < b[0] or a[1] < [1]:
#         check = False
#     elif a[0] > b[0] and a[1] > (b[1]) + b[3]):
#         check = False
#     elif a[1] > b[1] and a[0] > (b[0]) + b[2]):
#         check = False
#     else:
#         check = True
#     print(check)

# is_inside([200, 120], [140, 60, 100, 200])

def is_inside(a,b):
    check = True
    if b[0] > a[0] or b[1] > a[1]:
        check = False
    else:
        check = True
    print(check)

is_inside([200, 120], [140, 60, 100, 200])