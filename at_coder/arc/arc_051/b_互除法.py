# 色々試して素因数分解だの
# なんだのかんだのやってみたらわかりそう。
# fibだと、、、

# def gcd(a, b, c=0):
#     if b == 0:
#         return a, c
#     print(a, b)
#     return gcd(b, a%b, c+1)

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)

K = int(input())

print(fib(K+1), fib(K))

# print(gcd(fib(K+1), fib(K)))
