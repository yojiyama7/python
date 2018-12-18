N, M = map(int, input().split(" "))
UV = [list(map(int, input().split(" "))) for _ in range(M)]

d = [set() for _ in range(N+1)]
for u, v in UV:
    d[u].add(v)
    d[v].add(u)

visited = set()

def is_tree(n, before=None):
    if n in visited:
        return False
    visited.add(n)
    routes = d[n] - {before}
    if len(routes) == 0:
        return True
    return all([is_tree(route, n) for route in routes])

count = 0
for i in range(1, N+1):
    if i in visited:
        continue
    count += is_tree(i)
    # print(visited, count)

print(count)