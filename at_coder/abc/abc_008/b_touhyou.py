n = int(input())
a = [input() for i in range(n)]

print(max([(a_i, a.count(a_i)) for a_i in set(a)], key=lambda x: x[1])[0])