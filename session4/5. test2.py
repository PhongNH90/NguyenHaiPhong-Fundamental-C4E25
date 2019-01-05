nums = [-1,-2,4,7,5]

min_num = 999999999

for index, i in enumerate(nums):
    if i < min_num:
        min_num = i
        min_index = index

print(min_num)
print(min_index)

