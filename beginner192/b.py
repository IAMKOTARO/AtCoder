S = input()

for i, s in enumerate(S):
    if i % 2 == 0 and s.isupper():
        print('No')
        exit(0)
    elif i % 2 == 1 and s.islower():
        print('No')
        exit(0)

print('Yes')
