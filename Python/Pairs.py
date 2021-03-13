if __name__ == '__main__':
    n, k = input().split()
    k = int(k)
    val = input().split()
    a = [int(s) for s in val]
    b = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            b.append(a[i] * a[j])
    b.sort()
    print(b[k-1])