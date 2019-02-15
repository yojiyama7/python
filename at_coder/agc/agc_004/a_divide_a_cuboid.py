ABC = list(map(int, input().split(" ")))

if all(m%2 for m in ABC):
    x, y = sorted(ABC)[:2]
    # print(ABC)
    print(x*y)
else:
    print(0)

################################

# A, B, C = map(int, input().split(" "))

# x, y = sorted(ABC)[:2]
# print(x*y*(A%2)*(B%2)*(C%2))
