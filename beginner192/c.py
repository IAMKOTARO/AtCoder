N, K = map(int, input().split())


def g_1(x:str):
    if x == '0': return 0
    x_intlist = [int(s) for s in x]
    x_intlist.sort(reverse=True)
    return int(''.join(map(str, x_intlist)))


def g_2(x:str):
    if x == '0': return 0
    x_intlist = [int(s) for s in x]
    x_intlist.sort()
    for s in x_intlist:
        if s == 0:
            x_intlist = x_intlist[1:]
        else:
            break
    return int(''.join(map(str, x_intlist)))


def f(x:str):
    return str(g_1(x) - g_2(x))


a = [str(N)]
for i in range(1, K+1):
    a.append(f(a[i-1]))

print(a[-1])
