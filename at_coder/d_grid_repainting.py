# 幅優先探索(BFS)で最短ルートを求め、そのルートに必要のないセルをスコアとする

h, w = map(int, input().split(" "))
s_data = [input() for i in range(h)]
