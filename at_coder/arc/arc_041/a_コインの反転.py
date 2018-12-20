# 表にできない枚数: abs(Y-K)
X, Y = map(int, input().split(" "))
K = int(input())

print(X+Y-abs(Y-K))
