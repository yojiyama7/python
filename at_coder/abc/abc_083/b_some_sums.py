n, a, b = [int(m) for m in input().split(" ")]

some_sum = 0
for i in range(n+1):
    if a <= sum([int(m) for m in str(i)]) <= b:
        some_sum += i

print(some_sum)