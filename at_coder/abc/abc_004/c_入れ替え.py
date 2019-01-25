N = int(input())

nums = list("123456")

m = N//5%6
nums = nums[m:] + nums[:m]
for i in range(N%5):
    nums[i], nums[i+1] = nums[i+1], nums[i]

print("".join(nums))