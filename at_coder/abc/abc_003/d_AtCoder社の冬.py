R, C = map(int, input().split(" "))
X, Y = map(int, input().split(" "))
D, L = map(int, input().split(" "))

def p(n, k):
    m = 1
    for i in range(n, N-k, -1):
        if i == 0:
            break
        m *= i
    return m
def c(n, k):
    return p(n, k) // p(k, k)
def d(n, a, b):
    return c(N, a) * C(N-a, b)

q = d(X*Y, D, L)
q -= d((X-1)*Y, D, L)*2 + d(X*(Y-1), D, L)*2