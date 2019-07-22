# 誤字ミスしたから情報をテーブルやリストにまとめても良いかも

from math import factorial as fact

R, C = map(int, input().split(" "))
X, Y = map(int, input().split(" "))
D, L = map(int, input().split(" "))

def p(n, k):
    return fact(n) // fact(n-k)
def c(n, k):
    return p(n, k) // fact(k)
def q(w, h):
    if w < 0 or h < 0 or w*h < D+L:
        return 0
    return c(w*h, D) * c(w*h-D, L)
    # return fact(w*h) // fact(D) // fact(L) // fact(w*h-D-L)
# def q(x, y):
#     k=max(x,0)*max(y,0)
#     if k<D+L:
#         return 0
#     else:
#         return fact(k)//(fact(D)*fact(L)*fact(k-D-L))

pattern = q(X, Y)
# print(pattern)
pattern -= q(X-1, Y)*2 + q(X, Y-1)*2
# print(pattern)
pattern += q(X-1, Y-1)*4 + q(X-2, Y) + q(X, Y-2)
# print(pattern)
pattern -= q(X-2, Y-1)*2 + q(X-1, Y-2)*2
# print(pattern)
pattern += q(X-2, Y-2)
# print(pattern)

floor_pattern = (R-X+1)*(C-Y+1)
# print(pattern * floor_pattern, len(str(pattern * floor_pattern)))
print((pattern * floor_pattern)%(10**9+7))

################################

# AC コピペ

# r,c=map(int,input().split())
# x,y=map(int,input().split())
# d,l=map(int,input().split())

# def kaijo(x):
#     a=1
#     for i in range(1,x+1):
#         a*=i
#     return a
# if d+l==x*y:
#     ans=kaijo(d+l)//(kaijo(d)*kaijo(l))
#     ans*=(r-x+1)*(c-y+1)
#     print(int(ans%(10**9+7)))
# else:
#     def ans(x,y):
#         k=max(x,0)*max(y,0)
#         if k<d+l:
#             return 0
#         else:
#             return kaijo(k)//(kaijo(d)*kaijo(l)*kaijo(k-d-l))
#     t=(r-x+1)*(c-y+1)
#     a=ans(x,y)
#     b=ans(x-1,y)*2
#     c=ans(x,y-1)*2
#     D=ans(x-2,y)
#     e=ans(x,y-2)
#     f=ans(x-1,y-1)*4
#     g=ans(x-2,y-1)*2
#     h=ans(x-1,y-2)*2
#     i=ans(x-2,y-2)
#     # print(t*(a-b-c+D+e+f-g-h+i), len(str(t*(a-b-c+D+e+f-g-h+i))))
#     print(t*(a-b-c+D+e+f-g-h+i)%(10**9+7))

################################