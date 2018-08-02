n = int(input())
a = [tuple(map(int, input().split(" "))) for i in range(2)]

up_line, down_line = a

max_num = 0
for i in range(n):
	num = sum(up_line[:i+1]) + sum(down_line[i:])
	if max_num < num:
		max_num = num
print(max_num)