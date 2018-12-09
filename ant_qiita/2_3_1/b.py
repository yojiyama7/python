n = int(input())
s = list(map(int, input().split(" ")))

bit = 1
for s_i in s:
	bit |= bit<<s_i

print(bin(bit).count("1"))