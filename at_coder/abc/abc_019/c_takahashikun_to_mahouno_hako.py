n = int(input())
a = list(map(int, input().split(" ")))

odd_set = set()
for a_i in a:
	while a_i%2 == 0:
		a_i //= 2
	odd_set.add(a_i)

print(len(odd_set))