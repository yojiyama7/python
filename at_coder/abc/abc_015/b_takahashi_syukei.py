import math

n = int(input())
a = list(map(int, input().split(" ")))

while 0 in a:
    a.remove(0)
print(math.ceil((sum(a))/len(a)))