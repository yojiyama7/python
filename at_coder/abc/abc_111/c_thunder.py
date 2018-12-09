from collections import Counter

N = int(input())
V = list(map(int, input().split(" ")))

even, odd = [sorted(Counter(V[i::2]).items(), key=lambda x: x[1], reverse=True) + [[None, 0]] for i in range(2)]
# print(even, odd)
if even[0][0] == odd[0][0]:
	print(min(N-even[0][1]-odd[1][1], N-even[1][1]-odd[0][1]))
else:
	print(N-even[0][1]-odd[0][1])