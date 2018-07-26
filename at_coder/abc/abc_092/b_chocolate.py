n = int(input())
d, x = [int(m) for m in input().split(" ")]
a = [int(input()) for i in range(n)]

print(x + sum([(d-1)//a_i+1 for a_i in a]))