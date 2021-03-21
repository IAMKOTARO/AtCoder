N = input()
N_len = len(N)
count = 0
if N_len >= 2 and N_len < 4:
    for i in range(10**1, int(N)):
        if len(str(i))%2 == 0:
            i_str = str(i+1)
            if i_str[int(len(i_str)/2):] == i_str[:int(len(i_str)/2)]:
                count += 1
        else:
            break
if N_len >= 4 and N_len < 6:
    count += 9
    for i in range(10**3, int(N)):
        if len(str(i+1))%2 == 0:
            i_str = str(i+1)
            if i_str[int(len(i_str)/2):] == i_str[:int(len(i_str)/2)]:
                count += 1
        else:
            break
if N_len >= 6 and N_len < 8:
    count += 99
    for i in range(10**5, int(N)):
        if len(str(i+1))%2 == 0:
            i_str = str(i+1)
            if i_str[int(len(i_str)/2):] == i_str[:int(len(i_str)/2)]:
                count += 1
        else:
            break
if N_len >= 8 and N_len < 10:
    count += 999
    for i in range(10**7, int(N)):
        if len(str(i+1))%2 == 0:
            i_str = str(i+1)
            if i_str[int(len(i_str)/2):] == i_str[:int(len(i_str)/2)]:
                count += 1
        else:
            break
if N_len >= 10 and N_len < 12:
    count += 9999
    for i in range(10**9, int(N)):
        if len(str(i+1))%2 == 0:
            i_str = str(i+1)
            if i_str[int(len(i_str)/2):] == i_str[:int(len(i_str)/2)]:
                count += 1
        else:
            break
if N_len >= 12 and N_len < 14:
    count += 99999
    for i in range(10**11, int(N)):
        if len(str(i+1))%2 == 0:
            i_str = str(i+1)
            if i_str[int(len(i_str)/2):] == i_str[:int(len(i_str)/2)]:
                count += 1
        else:
            break
print(count)
