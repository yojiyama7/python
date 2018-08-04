import sys

n = int(input())
# a = map(int, sys.stdin.read().split("\n"))
a = map(int, [int(input()) for i in range(n)])

d = dict()
for a_i in a:
	if a_i not in d:
		d[a_i] = 0
	d[a_i] = (d[a_i]+1) % 2

print(sum(d.values()))