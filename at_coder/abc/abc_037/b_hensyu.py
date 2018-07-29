n, q = map(int, input().split(" "))
lrt = [tuple(map(int, input().split(" "))) for i in range(q)]

nums = [0]*n

for lrt_i in lrt:
	l, r, t = lrt_i
	nums[l-1:r] = [t]*(r-l+1)

for num in nums:
	print(num)