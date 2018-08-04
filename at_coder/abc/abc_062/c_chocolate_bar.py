import math

h, w = list(map(int, input().split(" ")))

if h%3 == 0 or w%3 == 0:
	print(0)
else:
	min_num = h*w
	