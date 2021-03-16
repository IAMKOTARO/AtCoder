X = input()
M = int(input())

count = 0
X_intlist = list(map(int, X))
X_max = max(X_intlist)
base_n = X_max + 1

while True:
    base_n_val = 0
    for i, x in enumerate(reversed(X_intlist)):
        base_n_val += x * (base_n ** i)
        if base_n_val > M: break
    if base_n_val > M:
        break
    else:
        count += 1
        base_n += 1

print(count)
