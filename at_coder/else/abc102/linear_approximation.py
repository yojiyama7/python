n = int(input())
a = [int(str_) for str_ in input().split(" ")]

print([abs(a_i-(i+1)) for i, a_i in enumerate(a)])