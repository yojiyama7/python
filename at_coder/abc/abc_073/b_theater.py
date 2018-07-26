n = int(input())
l_r = [[int(m) for m in input().split(" ")] for i in range(n)]

print(sum([r_i-l_i for l_i, r_i in l_r]) + n)