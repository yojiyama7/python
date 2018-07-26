n, m, x = [int(m) for m in input().split(" ")]
a = [int(m) for m in input().split(" ")]

x_more = [x < a_i for a_i in a]

print(min(x_more.count(True), x_more.count(False)))