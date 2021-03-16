n =  int(input())

def prime_factorize(n):
    a = []
    if n == 1:
        return [1]
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

print(prime_factorize(n))
# count = 0
# for i in range(n):
#     factonize_list = prime_factorize(i+1)
#     if len(factonize_list) == 1:
#         count += 1
#     elif len(list(set(factonize_list))) > 1:
#         count += 1
#     else:
#         print(i+1)
#         # print(f'{i+1} -> {prime_factorize(i+1)} {factonize_list[0]} ^ {len(factonize_list)}')
# # print(count)

