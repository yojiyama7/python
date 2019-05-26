R, D, X2000 = map(int, input().split(" "))

x = X2000
for i in range(10):
    x = R*x - D 
    print(x)