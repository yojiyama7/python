N = int(input())

digits_sum = lambda x: sum(map(int, str(x)))

min_num = 10**18
# rangeの上限を的確に決めれない、、、
for i in range(1, (N+1)//2+1):
    # print(i)
    m = N-i
    l = digits_sum(i) + digits_sum(m)
    min_num = min(l, min_num)

print(min_num)