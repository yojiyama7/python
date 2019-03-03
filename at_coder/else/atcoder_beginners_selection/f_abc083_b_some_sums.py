N, A, B = map(int, input().split(" "))

sum_num = 0
for i in range(1, N+1):
    if A <= sum(map(int, str(i))) <= B:
        sum_num += i

print(sum_num)