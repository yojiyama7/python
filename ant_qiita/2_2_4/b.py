# LISと同じ構造だが、、、
# 枠数を少なくしようとすることで、最長増加部分列(LIS)の長さが取れるということか、、、？

from bisect import bisect_left

BIG_NUM = 10**9

n = int(input())
w = [int(input()) for _ in range(n)]

l = [BIG_NUM] * n
for w_i in w:
	l[bisect_left(l, w_i)] = w_i

print(bisect_left(l, BIG_NUM))

################################

# n = int(input())
# w = [int(input()) for _ in range(n)]

# l = []
# for w_i in w:
# 	is_repl = False
# 	for j in range(0, len(l)):
# 		if l[j] >= w_i:
# 			l[j] = w_i
# 			is_repl = True
# 			break
# 	if is_repl == False:
# 		l.append(w_i)
# 	# print(l)

# print(len(l))