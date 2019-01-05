prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}

x = 0
for k in prices.keys():
    print(k)
    print("prices: ", prices[k] )
    print("stock: ", stock[k])
    total = prices[k] * stock[k]
    print("Total", k, ":", total)
    print()
    x += total

print("Total revenue: ", x)

# banana #prices[""]
#     prices 4
#     stock 6