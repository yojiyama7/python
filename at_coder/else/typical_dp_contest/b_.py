A, B = map(int, input().split(" "))
AL, BL = [list(map(int, input().split(" "))) for _ in range(2)]

l = [[-1 for _ in range(1010)] for _ in range(1010)]
l[A][B] = 0
def solve(i, j):
    # print(i, j)
    if l[i][j] != -1:
        return l[i][j]
    if (i+j)%2 == 0:
        l[i][j] = 0
        if i < A:
            l[i][j] = max(solve(i+1, j) + AL[i], l[i][j])
        if j < B:
            l[i][j] = max(solve(i, j+1) + BL[j], l[i][j])
    else:
        # HELP: なぜ大きな数で？
        l[i][j] = 10**18
        if i < A:
            l[i][j] = min(solve(i+1, j), l[i][j])
        if j < B:
            l[i][j] = min(solve(i, j+1), l[i][j])
    return l[i][j]

print(solve(0, 0))

################################

# A, B = map(int, input().split(" "))
# AL, BL = [list(map(int, input().split(" "))) for _ in range(2)]

# l = [[None for _ in range(1010)] for _ in range(1010)]
# def point(a_i, b_i, p):
#     print(a_i, b_i, p)
#     if a_i == b_i == -1:
#         return 0
#     if l[a_i][b_i] != None:
#         return l[a_i][b_i]
#     nums = []
#     if a_i > -1:
#         nums.append(point(a_i-1, b_i, not p) + AL[a_i])
#     if b_i > -1:
#         nums.append(point(a_i, b_i-1, not p) + BL[b_i])
#     l[a_i][b_i] = max(nums)
#     return l[a_i][b_i]

# point(A-1, B-1, 0)
