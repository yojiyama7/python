N = int(input())
T = [int(input()) for _ in range(N)]

# 全探索やつー わすれとったー
min_num = 10**8
for i in range(1<<N):
    ab = [0, 0]
    for j in range(N):
        ab[(i>>j)%2] += T[j]
    min_num = min(min_num, max(ab))
print(min_num)