# 頂点1に属した頂点たちから、2つ選んで最短ルートさがして、その2頂点の頂点1まで距離を足す
# 全通りやって最短を出力 までは見たことあるんだけど
# 実装がねぇ、、、

N, M = map(int, input().split(" "))
UVL = [tuple(map(int, input().split(" "))) for _ in range(m)]

