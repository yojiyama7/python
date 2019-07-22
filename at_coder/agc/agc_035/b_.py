from collections import deque

N, M = map(int, input().split(" "))
AB = [list(map(int, input().split(" "))) for _ in range(M)]

if M%2 == 1:
    print(-1)
    exit()

d = dict()
for a, b in AB:
    if a not in d:
        d[a] = []
    if b not in d:
        d[b] = []
    d[a].append(b)
    d[b].append(a)

# print(d)

q = deque()
for k, v in d.items():
    if len(v) == 1:
        q.append(k)

if 1 not in q:
    q.append(1)

# print(q)

l = []
while q:
    node = q.popleft()
    to_nodes = d[node]
    if len(to_nodes) % 2 == 1:
        to_node = to_nodes.pop()
        l.append((to_node, node))
        d[to_node].remove(node)
    for i in range(len(to_nodes)):
        to_node = to_nodes.pop()
        l.append((node, to_node))
        d[to_node].remove(node)
        if len(d[to_node]) != 0:
            q.append(to_node)

# print(l)
for c, d in l:
    print(c, d)