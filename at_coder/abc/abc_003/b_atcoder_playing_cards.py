s, t = [input() for i in range(2)]

for s_i, t_i in zip(s, t):
    if not 0 < len(set("@atcoder" if s_i=="@" else s_i) & set("@atcoder" if t_i=="@" else t_i)):
        print("You will lose")
        exit()
print("You can win")