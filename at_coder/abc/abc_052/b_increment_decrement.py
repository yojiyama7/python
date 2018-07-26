n = int(input())
s = input()

x = 0
x_max = 0
for n_i in range(n):
    x += 1 if "I" == s[n_i] else -1
    if x_max < x:
        x_max = x
print(x_max)