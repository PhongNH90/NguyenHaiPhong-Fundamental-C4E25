# def get_even_list(l):
#     for i in l:
#         if i % 2 != 0:
#             l.remove(i)
#         print(l)

# get_even_list([1, 4, 5, 9, 10])

def get_even_list(l):
    new_list = []
    for i in l:
        if i % 2 == 0:
            new_list.append(i)
    print(new_list)

get_even_list([1, 4, 5, 9, 10])