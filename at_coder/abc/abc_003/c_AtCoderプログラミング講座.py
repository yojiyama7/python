N, K = map(int, input().split(" "))
R = list(map(int, input().split(" ")))

R.sort()

sum_num = 0
for r in R[-K:]:
    sum_num = (sum_num + r) / 2

print(sum_num)