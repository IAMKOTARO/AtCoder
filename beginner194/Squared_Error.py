N = int(input())
A = [ int(i) for i in input().split() ]
 
ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans += (A[i] - A[j]) ** 2
print(ans)