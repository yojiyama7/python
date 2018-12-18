N, A, B = map(int, input().split(" "))

print(min(5, N)*B + (N-min(5, N))*A)