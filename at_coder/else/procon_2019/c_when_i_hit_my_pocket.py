K, A, B = map(int, input().split(" "))

if B-A >= 3:
    # マイナスになりうる
    l = K-(A-1)
    # print(l, (B-A)*(l//2))
    print(A+(B-A)*(l//2)+l%2)
else:
    print(K+1)