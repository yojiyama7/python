# もうちょいでは？

t = input()

sum_num = 0
l_a = 0
l_q = 0
r_c = t.count("C")
r_q = t.count("?")
for i, t_i in enumerate(t):
    if t_i == "C":
        r_c -= 1
    elif t_i == "?":
        r_q -= 1
    
    if t_i == "B" or t_i == "?":
        print(i, t_i, (l_a + l_q) * (r_c + r_q))
        sum_num = (sum_num + ((l_a + l_q) * (r_c + r_q)) * 2**(r_q)) % (10**9+7)
    
    if t_i == "A":
        l_a += 1
    elif t_i == "?":
        l_q += 1

print(sum_num)