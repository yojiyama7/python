n, x = map(int, input().split(" "))
a = tuple(map(int, input().split(" ")))

x_2_str = ""
while x:
    x_2_str += str(x%2)
    x //= 2
print(sum([a_i*int(x_i) for x_i, a_i in zip(x_2_str, a)]))