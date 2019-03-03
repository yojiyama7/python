S = input()
n = len(S)-1

sum_num = 0
for i in range(1<<n):
    t = S[0]
    for j in range(n):
        if (i>>j)%2:
            t += "+"
        t += S[j+1]
    sum_num += eval(t)

print(sum_num)