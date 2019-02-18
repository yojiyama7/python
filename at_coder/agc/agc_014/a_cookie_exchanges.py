# # AC
# BIG_NUM = 10**18
# is_even = lambda x: x%2==0
# def two_count(x):
#     if x == 0:
#         return BIG_NUM
#     c = 0
#     while x and x%2 == 0:
#         x //= 2
#         c += 1
#     return c
    
# A, B, C = map(int, input().split(" "))

# if all(map(is_even, [A, B, C])):
#     a2, b2, c2 = (B+C)//2, (C+A)//2, (A+B)//2    
#     n = min(map(two_count, [A-a2, B-b2, C-c2]))
#     if n == BIG_NUM:
#         print(-1)
#     else:
#         print(n+1)
# else:
#     print(0)

################################

# # WA
# a,b,c=map(int,input().split())
# if a==b==c:print(-1)
# else:
#  r=0
#  while-~a*-~b*-~c%2:
#   a,b,c,r=(b+c)//2,(c+a)//2,(a+b)//2,r+1
#  print(r)