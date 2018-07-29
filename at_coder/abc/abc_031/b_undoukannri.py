l, h = map(int, input().split(" "))
n = int(input())
a = [int(input()) for i in range(n)]

for a_i in a:
	if a_i < l:
		print(l-a_i)
	elif h < a_i:
		print(-1)
	else:
		print(0)