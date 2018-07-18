# import sys

# k = int(sys.stdin.readline())

# n = 0
# while n < k:
# 	print(n%9+1, end="")
# 	print(n//9*"9")
# 	n += 1

nums_list = []
for k in range(1, 10000000):
	digits = []
	remaining_num = k
	while 0 != remaining_num:
		digits.append(remaining_num % 10)
		remaining_num //= 10
	nums_list.append((k, digits, k/sum(digits)))

for i, nums in enumerate(nums_list):
	if nums[2] <= min([nums[2] for nums in nums_list[i+1:]]):
		print(nums)
	if i == 800000:
		break

[9] 1 2 3 4 5 6 7 8 9 
[9] 19 29 39 49 59 69 79 89 99
[9] 199 299 399 499 599 699 799 899 999

[] 1099 1199 1299 1399 1499 1599 1699 1799 1899 1999
