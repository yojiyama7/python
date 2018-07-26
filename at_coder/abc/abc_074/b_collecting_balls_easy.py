n = int(input())
k = int(input())
x = [int(m) for m in input().split(" ")]

walk_sum = 0
for n_i in range(n):
    walk_sum += min(2*x[n_i], 2*(k-x[n_i]))

print(walk_sum)