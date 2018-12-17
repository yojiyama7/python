N, M, L = map(int, input().split(" "))
P, Q, R = map(int, input().split(" "))

print(max(
    (N//P)*(M//Q)*(L//R),
    (N//P)*(M//R)*(L//Q),
    (N//Q)*(M//P)*(L//R),
    (N//Q)*(M//R)*(L//P),
    (N//R)*(M//P)*(L//Q),
    (N//R)*(M//Q)*(L//P),
))