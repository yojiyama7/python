N = int(int(input()))
C_S_F = [list(map(int, input().split(" "))) for _ in range(N-1)]

for i in range(N-1):
	time = 0
	for j in range(i, N-1):
		c, s, f = C_S_F[j]
		time = max(s, time + abs(time%-f))
		time += c
	print(time)
print(0)

################################

# N = int(int(input()))
# C_S_F = [list(map(int, input().split(" "))) for _ in range(N-1)]

# # print(f"C_S_F: {C_S_F}")

# for i in range(N-1):
# 	time = 0
# 	for j in range(i, N-1):
# 		c, s, f = C_S_F[j]
# 		# print(time, "c,s,f:", c, s, f)
# 		time = max(s, time + abs(time%-f))
# 		# print(s, time + abs(time%-f))
# 		time += c
# 		# print(time)
# 	# 	print("---")
# 	# print("#")
# 	print(time)

# print(0)