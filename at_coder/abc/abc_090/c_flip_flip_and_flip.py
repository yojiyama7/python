n, m = map(int, input().split(" "))

n_ = 1 if n == 1 else n-2
m_ = 1 if m == 1 else m-2
print(n_*m_)

# 実際にリストで再現(左右上下1マスを除いた部分を参照する)
# nums = [[0] * (m+2) for i in range(n+2)]
# for y in range(1, n+1):
# 	for x in range(1, m+1):
# 		for x_adjust, y_adjust in [(a, b) for b in range(-1, 2) for a in range(-1, 2)]:
# 			nums[y+y_adjust][x+x_adjust] = (nums[y+y_adjust][x+x_adjust]+1)%2

# for num in nums:
# 	print(num)
