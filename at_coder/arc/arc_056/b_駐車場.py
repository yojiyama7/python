# なぜだ？？？
# わからん、、、
import sys

sys.setrecursionlimit(10**8)

N, M, S = map(int, input().split(" "))
UV = [list(map(int, input().split(" "))) for _ in range(M)]

t = [set() for _ in range(N+1)]
for u, v in UV:
    t[u].add(v)
    t[v].add(u)

visited = [False for _ in range(N+1)]
visited[S] = True
def dfs(n):
    routes = t[n]
    for route in routes:
        if visited[route] or route > n:
            continue
        # if route > n and visited[route] == None:
        #     visited[route] = False
        # else:
        #     visited[route] = True
        visited[route] = True
        dfs(route)

dfs(S)
# print(visited)
for i in range(1, N+1):
    if visited[i]:
        print(i)
