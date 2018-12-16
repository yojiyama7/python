N = int(input())
C = input()

l = [C.count(s) for s in "1234"]
# print(C, l)
print(max(l), min(l))