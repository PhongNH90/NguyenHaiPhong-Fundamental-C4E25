def is_inside(a,b):
    check = 1
    if b[0] > a[0] or b[1] > a[1]:
        check = 0
    else:
        check = 1
    return check

check_list = is_inside([200, 120], [140, 60, 100, 200])

if check_list == 1:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
