# 数学式的なアプローチはあるが、それを理解しきれない
def f(h, w):
    l = []
    for i in range(w):
        m = [(w-i)*h, i*(h//2), i*(h-h//2)]
        l.append(max(m)-min(m))
    # print(l)
    return min(l)

H, W = map(int, input().split(" "))

if 0 in [H%3, W%3]:
    print(0)
else:
    # T字分割縦, T字分割横、3列分割縦、3列分割横
    print(min(f(H, W), f(W, H), H, W))

################################

# よく理解できないぞ

# H, W = map(int, input().split(" "))

# s = [h//2+w//3+1, h//3+w//2+1, h, w]
