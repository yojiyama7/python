from bisect import bisect_right

N = int(input())

l = [int(str(i%9+1)+"9"*(i//9)) for i in range(9*16)]

print(bisect_right(l, N))