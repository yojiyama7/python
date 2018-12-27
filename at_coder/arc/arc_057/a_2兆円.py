A, K = map(int, input().split(" "))

if K == 0:
    print(2*(10**12)-A)
    exit()

count = 0
while A < 2*(10**12):
    A += A*K+1
    count += 1

print(count)