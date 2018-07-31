abc = list(map(int, input().split(" ")))

count = 0
while True:
	abc.sort()

	if abc[0] == abc[1] == abc[2]:
		break
	elif abc[0] == abc[1]:
		abc[0] += 1
		abc[1] += 1	
		count += 1
	else:
		abc[0] += 2
		count += 1

print(count)