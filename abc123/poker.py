import collections

k = int(input())
s = input()
t = input()

def calc_point(cards):
    point = 0
    card_list = [s for s in cards]
    collect_dict = collections.Counter(card_list)
    # print(f'{cards} -> {collect_dict}')
    for i in range(9):
        if str(i+1) in collect_dict.keys():
            point += (i+1) * 10 ** collect_dict[str(i+1)]
        else:
            point += i+1
    return point

cards_remaining = [int(k)] * 9
for i, j in zip(s[:-1], t[:-1]):
    cards_remaining[int(i)-1] -= 1
    cards_remaining[int(j)-1] -= 1
print(cards_remaining)
takahasi_possible_point_list = []
aoki_possible_point_list = []
for i in range(9):
    if cards_remaining[i-1]:
        s_temp= s[:-1] + str(i+1)
        t_temp = t[:-1] + str(i+1)
        takahasi_possible_point_list.append(calc_point(s_temp))
        aoki_possible_point_list.append(calc_point(t_temp))

num_total_fitting = 9**2
takahasi_win = 0
for taka in takahasi_possible_point_list:
    for ao in aoki_possible_point_list:
        if taka > ao:
            takahasi_win += 1

# print(f'{takahasi_win}/{num_total_fitting}') 
# print(takahasi_win/num_total_fitting)
