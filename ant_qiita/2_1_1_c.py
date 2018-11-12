d, g = map(int, input().split(" "))
pc = [list(map(int, input().split(" "))) for _ in range(d)]

# pc_ = [(pc_i[0]*100+pc[1])/pc_i[0] for pc_i in pc]
pc = [pc_i + [None, (100*(i+1))*pc_i[0] + pc_i[1]] for i, pc_i in enumerate(pc)]

count = 0
while g > 0:
	for i, pc_i in enumerate(pc):
		num, bonus, per_one, total = pc_i
		if num == 0:
			pc[i] = []
		if (100*(i+1))*(num-1) < g:
			pc[i][2] = total / num
		else:
			pc[i][2] = 100*(i+1)
	max_q = max(pc, key=lambda x: x[2])
	print(pc)
	count += (g -1)//max_q[2] +1
	g -= max_q[2]

print(count)