N, M = map(int, input().split(" "))
XYZ = [list(map(int, input().split(" "))) for _ in range(M)]

l = [[] for _ in range(N)]
for x, y, _ in XYZ:
    l[x-1].append(y-1)
    l[y-1].append(x-1)

visited = [False]*N
count = 0
for i in range(N):
    # 訪れたことがあれば
    if visited[i] == True:
        continue
    visited[i] = True
    q = l[i]
    while q:
        r = []
        for y in q:
            if visited[y] == True:
                continue
            visited[y] = True
            r += l[y]
        q = r
        # print(q)
    count += 1
    # print(i, count, visited)

# print(count, visited)
print(count)

        
