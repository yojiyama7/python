n = int(input())
s_p = [input().split(" ") for i in range(n)]

max_s_p = max(s_p, key=lambda x: int(x[1]))
if sum([int(s_p_i[1]) for s_p_i in s_p]) < int(max_s_p[1])*2:
	print(max_s_p[0])
else:
	print("atcoder")