if __name__ == '__main__':
    a,b,c = input().split()
    if not a == b == c:
        if a == b:
            print('Yes')
        elif b == c:
            print('Yes')
        elif a == c:
            print('Yes')
        else:
            print('No')
    else:
        print('No')