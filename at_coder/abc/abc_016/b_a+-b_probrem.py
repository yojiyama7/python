a, b, c = map(int, input().split(" "))

if c in (a+b, a-b):
    if a+b == a-b:
        print("?")
    else:
        print("+-"[(a+b, a-b).index(c)])
else:
    print("!")