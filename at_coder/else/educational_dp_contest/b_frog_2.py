# pythonでDPするならzip使わないとダメ?

N, K = map(int, input().split(" "))
H = list(map(int, input().split(" ")))

costs = [0]*(N+10)
for i in range(1, N):
    j = max(0, i-K)
    h_i = H[i]
    costs[i] = min(cost+abs(h_i-h) for cost, h in zip(costs[j:i], H[j:i]))

print(costs[N-1])

################################

# # TLE

# BIG_NUM = 10**18

# N, K = map(int, input().split(" "))
# H = list(map(int, input().split(" ")))

# l = [BIG_NUM]*(N+200)
# l[0] = 0
# for i in range(1, N):
#     l[i] = min([
#         l[i-j] + abs(H[i]-H[i-j]) for j in range(1, min(N, K, i)+1)
#     ])

# # print(l)
# print(l[N-1])