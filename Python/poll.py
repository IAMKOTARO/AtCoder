# coding: utf-8
if __name__ == '__main__':
    dic = dict()
    n = int(input())
    for i in range(n):
        val = input()
        if val in dic.keys():
            dic[val]+=1
        else:
            dic[val]=1
    max_keys = max(dic.values())
    values_of_max_key = [val for val in dic if dic[val] == max_keys]
    sorted_values_of_max_key = sorted(values_of_max_key)
    for s in sorted_values_of_max_key:
        print(s)