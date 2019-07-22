N = int(input())
A = list(map(int, input().split(" ")))

l = [0]*N
p = []
for i in range(N-1, -1, -1):
    m = sum(l[i::i+1])%2
    if A[i] == m:
        continue
    l[i] = 1
    p.append(i)

print(len(p))
for p_i in p:
    print(p_i+1)