n, k = map(int, input().split(" "))
a = tuple(map(int, input().split(" ")))

b = [0]
for a_i in a:
    b.append(b[-1]+a_i)
print(sum(b[-k:])-sum(b[:k]))