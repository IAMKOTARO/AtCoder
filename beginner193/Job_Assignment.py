import sys


N = int(input())
A = []
B = []

for i in range(N):
    a, b = input().split()
    A.append(int(a))
    B.append(int(b))

min_time = 2 * 10 ** 5

for i, a in enumerate(A):
    for j, b in enumerate(B):
        if i == j:
            if a+b < min_time:
                min_time = a+b
        else:
            if max(a, b) < min_time:
                min_time = max(a, b)

print(min_time)
