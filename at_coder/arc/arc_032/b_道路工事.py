import sys

sys.setrecursionlimit(10**8)

N, M = map(int, input().split(" "))
AB = [list(map(int, input().split(" "))) for _ in range(M)]

d = [set() for _ in range(N)]
for a, b in AB:
    d[a-1].add(b-1)
    d[b-1].add(a-1)

# not_visit = set(range(N))
visited = set()
def dfs(n):
    # print(not_visit)
    # not_visit.remove(n)
    visited.add(n)
    routes = d[n] - visited
    for route in routes:
        dfs(route)
        # d[route] = None

count = 0
for i in range(N):
    if i in visited:
        continue
    dfs(i)
    count += 1
print(count-1)