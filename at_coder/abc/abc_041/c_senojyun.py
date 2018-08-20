n = int(input())
a = tuple(map(int, input().split(" ")))

a = list(zip(range(1,len(a)+1), a))
a.sort(key=lambda x:x[1], reverse=True)
for a_i in a:
	print(a_i[0])