n, k = map(int, input().split(" "))
d = input().split(" ")

while set(str(n)) & set(d):
	n += 1
print(n)