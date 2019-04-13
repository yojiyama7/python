A, B, K = map(int, input().split(" "))

print([i for i in range(100, 0, -1) if A%i == B%i == 0][K-1])