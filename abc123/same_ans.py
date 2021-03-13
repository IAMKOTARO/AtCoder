with open('ans.txt', 'r') as ans_f, open('myans.txt', 'r') as my_f:
    ans = [s.replace('\n', '') for s in ans_f.readlines()]
    my = [s.replace('\n', '') for s in my_f.readlines()]

print(list(set(ans) - set(my)))