# 歩くコストと、塗るコストを別で考える
# 発想はいい、あとは実装。
N, R = map(int, input().split(" "))
S = list(input())

while (S) and S[-1] == "o":
    S.pop()
    N -= 1

p = 0
cost = 0
for i in range(N):
    if S[i] != ".":
        continue
    S[i:i+R] = ["o"]*R
    # print(S)
    p = i
    cost += 1

# print(cost, p, N-R)
cost += min(max(0, N-R), p)
print(cost)

################################
#-------------------------------
################################

# N, R = map(int, input().split(" "))
# S = list(input())

# # while S[-1] == "o":
# #     S.pop()
# #     N -= 1

# # print(S)

# p = 0
# cost = 0 #; print(cost)
# for i in range(N):
#     # if i-(R-1) < 0:
#     #     continue
#     print(i, S[i-(R-1)])
#     if S[i-(R-1)] != ".":
#         continue
#     S[i-(R-1):i+R] = ["o"]*(R*2-1)
#     print(S)
#     cost += i-p+1
#     print(cost)
#     p = i
# if S[-1] == ".":
#     cost += N-R-p+1

# print(cost)

################################

# i = 0
# cost = 0
# while i < N:
#     # print(i, end=" ")
#     if S[i] == "o":
#         i += 1
#         cost += 1
#         continue
#     i += R-1
#     last_action = i
#     print("a:",S)
#     S[i-R+1:i+R] = ["o"]*(2*R-1)
#     print("b:",S)
#     cost += R
#     print(cost, S)
# # cost -= len(S[N:])
# print(cost, N, i)
# cost -= N-i+1

# print(cost)