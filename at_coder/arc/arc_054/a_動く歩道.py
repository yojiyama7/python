# なんか余計なの入れて提出したな、まあええけど
L, X, Y, S, D = map(int, input().split(" "))

# print(D-S, (D-S)%L, X+Y)
# print(X, Y, X-Y)
if Y-X <= 0:
    print((D-S)%L/(Y+X))
else:
    # print(S-D, S-D%L, Y-X)
    print(min((D-S)%L/(Y+X), (S-D)%L/(Y-X)))