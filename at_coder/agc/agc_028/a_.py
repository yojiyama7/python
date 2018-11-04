# no submit

def gcd(n, m):
	if m < n:
		n, m = m, n
	while n:
		n, m = m%n, n
	return m
def lcm(n, m):
	return n*m // gcd(n, m)

n, m = map(int, input().split(" "))
s, t = [input() for _ in range(2)]

gcd_nm = gcd(n, m)
print(lcm(n, m) if s[::n//gcd_nm] == t[::m//gcd_nm] else -1)

# 6
# 2 3
# a__e__
# a_c_p_
# 最初の文字は同じ

# 6 3
# abcdef
# a_b_c_

# def gcd(n, m):
# 	if m < n:
# 		n, m = m, n
# 	while n:
# 		n, m = m%n, n
# 	return m
# def lcm(n, m):
# 	return n*m // gcd(n, m)

# n, m = map(int, input().split(" "))
# s, t = [input() for _ in range(2)]

# lcm_nm = lcm(n, m)
# s_ = "".join([s_i+"_"*(lcm_nm//n - 1) for s_i in s])
# t_ = "".join([t_i+"_"*(lcm_nm//m - 1) for t_i in t])
# for i in range(lcm_nm):
# 	if not (s_[i] in ["_", t_[i]] or t_[i] == "_"):
# 		print(-1)
# 		exit()
# print(lcm_nm)
