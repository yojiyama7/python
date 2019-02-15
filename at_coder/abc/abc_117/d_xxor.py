N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

# for a in A:
#     print(bin(a)[2:].rjust(6, "0"))

# Xは桁ごとに最適があるがK以下という制限があると、
# 最適が変わる可能性がある
x = 0
for i in range(39, -1, -1):
    b = sum((a>>i)%2 for a in A)*2 < N
    # print(b, b<<i)
    if x+(b<<i) <= K:
        x += (b<<i)
    else:
        continue

# for i in range(39, -1, -1):
#     if x <= K:
#         break
#     x = x&((1<<i)-1)

print(sum(x^a for a in A))