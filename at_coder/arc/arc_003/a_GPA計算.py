N = int(input())
S = input()

sum_num = 0
for i in range(5):
    sum_num += S.count("FDCBA"[i])*i

print(sum_num/N)