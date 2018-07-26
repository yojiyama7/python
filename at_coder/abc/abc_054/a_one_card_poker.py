a, b = map(int, input().split(" "))

a, b = [14 if 1==ab_i else ab_i for ab_i in (a, b)]
if a>b:
    print("Alice")
elif a<b:
    print("Bob")
else:
    print("Draw")