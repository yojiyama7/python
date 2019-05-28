N, K = map(int, input().split(" "))
V = list(map(int, input().split(" ")))

max_score = 0
for i in range(N+1):
    # print(list(range(i, N+1)))
    for j in range(i, N+1):
        # print(i, j)
        p = V[:i] + V[j:] 
        # print(p)
        if len(p) > K:
            continue
        p.sort(reverse=True)
        for _ in range(K-len(p)):
            if p and p[-1]<0:
                p.pop()
            else:
                break
        score = sum(p)
        # print(p)
        max_score = max(max_score, score)

print(max_score)