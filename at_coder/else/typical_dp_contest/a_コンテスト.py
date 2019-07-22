N = int(input())
P = list(map(int, input().split(" ")))

b = 1
for p in P:
    b |= b<<p
    b |= 1<<p
    # print(bin(b))

print(bin(b).count("1"))

