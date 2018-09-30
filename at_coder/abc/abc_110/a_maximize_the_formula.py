a, b, c = input()[::2]

print(max([
	int(b+c) + int(a),
	int(c+a) + int(b),
	int(a+b) + int(c)
]))