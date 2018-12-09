x, y = map(int, input().split(" "))

count = 0
while x <= y:
	count += 1
	x *= 2
	
print(count)

################################

# x, y = map(int, input().split(" "))

# count = 0
# while x <= y:
# 	count += 1
# 	x *= 2

# print(count)

################################
#---#---#---#---#---#---#---#---
################################

# import math

# x, y = map(int, input().split(" "))

# print(int(math.log(y/x, 2)) + 1) 