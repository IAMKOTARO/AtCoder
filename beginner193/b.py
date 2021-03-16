n = int(input())

min_price = 10 ** 9
for i in range(n):
    time, price, stock = [int(s) for s in input().split()]
    if (stock > time) and (min_price > price):
        min_price = price

if min_price != 10 ** 9:
    print(min_price)
else:
    print(-1)
