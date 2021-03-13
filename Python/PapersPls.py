if __name__ == '__main__':
    n = int(input())
    val = input()
    a = val.split()
    a = [int(s) for s in a]
    enter = True
    for i in a:
        if i % 2 == 0:
            if not (i % 3 == 0 or i % 5 == 0):
                enter = False
    if enter:
        print('APPROVED')
    else:
        print('DENIED')