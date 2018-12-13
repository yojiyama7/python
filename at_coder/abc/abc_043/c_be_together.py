# これでとおるんかーい
N = int(input())
A = list(map(int, input().split(" ")))

min_num = 100**2*N
for i in range(-100, 101):
	min_num = min(min_num, sum((a-i)**2 for a in A))
print(min_num)