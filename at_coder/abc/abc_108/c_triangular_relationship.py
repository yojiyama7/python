N, K = map(int, input().split(" "))

"""
i%K == 0 ならその数同士で条件に合う数列を作れる
i%K == K//2 ならその数同士で条件に合う数列を作れる(Kが偶数の場合)
これらは条件によって導ける
"""

count = (N//K)**3
if K%2 == 0:
	count += (N//K + (N%K >= K//2))**3
print(count)

