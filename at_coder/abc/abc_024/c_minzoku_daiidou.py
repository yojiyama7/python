# ただの貪欲法やんけ！！！　気づけ！！！
# 一つの民族の視点になれば、近づいていくだけ
# 目的が"最短"である場合、
# 単純に目的に近づいていくアルゴリズムが有効な可能性がある
N, D, K = map(int, input().split(" "))
LR = [tuple(map(int, input().split(" "))) for _ in range(D)]
ST = [tuple(map(int, input().split(" "))) for _ in range(K)]

for s, t in ST:
    for i, lr in enumerate(LR):
        l, r = lr
        if l <= s <= r:
            if l <= t <= r:
                print(i+1)
                break
            s = min(l, r, key=lambda x: abs(x-t))
                
