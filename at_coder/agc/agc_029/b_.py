# なんか解法違いそう
# 2のm乗のリスト(N=31)を使って
# A[i]と繫げることができるbを全て探索して記録
# 重みなし2部マッチング(重いか)

# 悲しきかな貪欲法の証明ができなかったぞ。

from collections import Counter

N = int(input())
A = list(map(int, input().split(" ")))

A_counter = Counter(A)
twos = [2**i for i in range(1, 32)]
# できるだけ大きい数から消費したいとすると
count = 0
for a in sorted(A_counter, reverse=True):
    for two in twos:
        if two <= a:
            continue
        b = two-a
        # if max(0, A_counter[b] - (a == b)) != 0:
        #     print(f"a: {a}, b: {b}, two: {two}")
        #     print(A_counter[b])

        if 0 <= A_counter[b] - (a == b):
            A_counter[a] -= 1
            A_counter[b] -= 1
            count += 1
            break
            

print(count)