#tham khảo bài của bạn Đặng Thu Huyền

import collections

x = input("Enter a string: ").lower()
c = collections.Counter(x)

for letter, count in sorted(c.items()):
    print(letter, count, sep="  ")