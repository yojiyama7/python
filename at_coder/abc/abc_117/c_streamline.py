N, M = map(int, input().split(" "))
X = list(map(int, input().split(" ")))

X.sort()
X_d = [X[i+1]-X[i] for i in range(M-1)]
X_d.sort()

# print(X_d, N)
print(sum(X_d[:max(0, M-N)]))