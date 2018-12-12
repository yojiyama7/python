N = int(input())
A = list(map(int, input().split(" ")))

two = 0
one = 0
zero = 0
for a in A:
	if a%4 == 0:
		two += 1
	elif a%2 == 0:
		one += 1
	else:
		zero += 1

print("Yes" if zero <= two+(one==0) else "No") 

################################

# # 原理がわからない

# n = int(input())
# a = tuple(map(int, input().split(" ")))

# than_2, than_1, than_0 = 0, 0, 0 
# for a_i in a:
# 	if a_i%4 == 0:
# 		than_2 += 1
# 	elif a_i%2 == 0:
# 		than_1 += 1
# 	else:
# 		than_0 += 1

# if n//2 <= than_2 + than_1//2:
# 	print("Yes")
# else:
# 	print("No")