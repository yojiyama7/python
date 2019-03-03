ABCD = input()

for i in range(1<<3):
    t = ABCD[0]
    for j in range(3):
        t += "+-"[(i>>j)%2]
        t += ABCD[j+1]
    if eval(t) == 7:
        print(t+"=7")
        exit()