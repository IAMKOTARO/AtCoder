X = int(input())

for i in range(100, 10**6, 10**2):
    if i > X:
        print(i-X)
        exit(0)
