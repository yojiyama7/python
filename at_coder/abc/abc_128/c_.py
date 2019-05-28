N, M = map(int, input().split(" "))
KS = [list(map(int, input().split(" "))) for _ in range(M)]
P = list(map(int, input().split(" ")))

s = [set(ks[1:]) for ks in KS]
# l = [set() for _ in range(N)]
# for i, ks in enumerate(KS):
#     s = ks[1:]
#     for s_i in s:
#         l[s_i-1].add(i)
# print(l)

count = 0
for i in range(1<<N):
    t = set()
    for j in range(N):
        if (i>>j)%2:
            t.add(j+1)
            # print(j, end="_")
    # print(t, [len(s_i & t)%2==0 for s_i in s], s)
    if all(len(s_i & t)%2==P[k] for k, s_i in enumerate(s)):
        count += 1
            

print(count)