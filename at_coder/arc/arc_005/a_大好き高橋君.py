N = int(input())
W = input().split(" ")

W[-1] = W[-1][:-1]
print(sum(W.count(s) for s in ["TAKAHASHIKUN", "Takahashikun", "takahashikun"]))