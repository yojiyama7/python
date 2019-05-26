N, K = map(int, input().split(" "))
S = input()

l = list(S)
l[K-1] = S[K-1].lower()
S = "".join(l)

print(S)