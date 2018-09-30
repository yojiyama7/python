n, s, t = map(int, input().split(" "))
a = [int(input()) for i in range(n)]

weight = 0
best_count = 0
for a_i in a:
	weight += a_i
	if s <= weight <= t:
		best_count += 1
print(best_count)

# n,s,t=map(int,input().split());w=0;c=0
# for i in range(n):
#  w+=int(input())
#  c+=s<=w<=t
# print(c)

# n,s,t=map(int,input().split());w=c=0
# for i in[0]*n:w+=int(input());c+=s<=w<=t
# print(c)