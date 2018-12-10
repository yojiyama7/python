print(max(for f,p in zip(input()[::2]for _ in range(N)))for i in range(1,1024)))

N = int(input())
F = [int(input().replace(" ", ""), 2) for _ in range(N)]
P = [list(map(int, input().split(" "))) for _ in range(N)]

max_num = -(10**9)
for i in range(1, 1<<10):
    point = 0
    for j in range(N):
        point += P[j][bin(i&F[j]).count("1")]
    # print(point, end=", ")
    # if max_num < point:
    #     print(bin(i), point)
    max_num = max(max_num, point)

print(max_num)

################################

# N=int(input());r=range;F=[int(input()[::2],2)for _ in r(N)];P=[list(map(int,input().split(" ")))for _ in range(N)];print(max(sum(p[bin(i&f).count("1")]for f,p in zip(F,P))for i in r(1,1024)))
