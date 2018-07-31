n = int(input())
s = input()

min_num = 300000
w_west = 0
e_east = s.count("E")
for s_i in s:
    if s_i == "E":
        e_east -= 1
    else:
        w_west += 1
    tmp = w_west + e_east - bool(s_i == "W")
    if tmp < min_num:
        min_num = tmp
print(min_num)