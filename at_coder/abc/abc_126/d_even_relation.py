N = int(input())
UVW = [list(map(int, input().split(" "))) for _ in range(N-1)]

d = dict()
for u, v, w in UVW:
    if u-1 not in d:
        d[u-1] = []
    if v-1 not in d:
        d[v-1] = []
    d[u-1] += [(v-1, w)]
    d[v-1] += [(u-1, w)]

visited = [False]*(N)
visited[0] = True
l = [0]*N
q = [0]
while q:
    # print(q, l, visited)
    len_q = len(q)
    for u in q[:]:
        for v, w in d[u]:
            if visited[v] == True:
                continue
            visited[v] = True
            if w%2 == 0:
                l[v] = l[u]
            else:
                l[v] = (l[u]+1)%2
            q.append(v)
    q = q[len_q:]
            # print(q)
    # print(q)

for m in l:
    print(m)