# https://abc089.contest.atcoder.jp/tasks/abc089_c

import copy

n = int(input())
s = [input().replace("\n", "") for i in range(n)]
march_num_list = [0, 0, 0, 0, 0]

for name in s:
    for i, head in enumerate(("M", "A", "R", "C", "H")):
        if name[0] == head:
            march_num_list[i] += 1

pattern_num = 0

for i in range((march_num_list)):
    two_list = copy.copy(march_num_list)
    two_list.pop(i)
    for j in range(len(two_list)):
        three_list = copy.copy(two_list)
        three_list.pop(j)
        for k in range(len(three_list)):
            pattern_num += three_list[0] * three_list[1] * three_list[2]

print(pattern_num)