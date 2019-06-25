# ウニみたいなグラフを作って、頂点1以外の2つの頂点を結ぶごとに最短距離2のペアが1減る
# これを書けば行ける。　無理なときは無理。

N, K = map(int, input().split(" "))

max_edge_count = (N-1)*(N-2)//2
if max_edge_count < K:
    print(-1)
    exit()

edges = []

for i in range(2, N+1):
    edges.append((1, i))

count = max_edge_count - K
for i in range(2, N+1):
    for j in range(i+1, N+1):
        if count == 0:
            print(len(edges))
            for edge in edges:
                print(*edge)
            exit()
        edges.append((i, j))
        count -= 1

print(len(edges))
for edge in edges:
    print(*edge)