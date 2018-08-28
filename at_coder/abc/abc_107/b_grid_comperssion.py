h, w = map(int, input().split(" "))
a = [input() for _ in range(h)]

h_remove_count = 0
while "."*w in a:
	a.remove("."*w)
	h_remove_count += 1

a = ["".join(h_line) for h_line in zip(*a)]
while "."*(h-h_remove_count) in a:
	a.remove("."*(h-h_remove_count))

for line in zip(*a):
	print("".join(line))