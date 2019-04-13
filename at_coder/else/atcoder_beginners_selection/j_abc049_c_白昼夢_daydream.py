S = input()

while S:
    l = [len(t) for t in ["dream", "dreamer", "erase", "eraser"] if S[-len(t):]==t]
    if l:
        S = S[:-l[0]]
    else:
        print("NO")
        exit()

print("YES")