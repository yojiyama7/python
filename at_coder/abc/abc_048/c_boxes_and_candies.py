# 後ろの方を減らした方が次に役立つよねってことね(貪欲法)

N, X = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

a += [0]

count = 0
for i in range(N):
    extra = a[i]+a[i+1] - X
    if extra <= 0:
        continue
    count += extra
    if a[i+1] >= extra:
        a[i+1] -= extra
    else:
        a[i] -= extra-a[i+1]
        a[i+1] = 0
    # print(a)
print(count)


################################
#-------------------------------
################################

# n, x = map(int, input().split(" "))
# a = tuple(map(int, input().split(" ")))

# a_in = [max(0, a[i] + a[i+1] - x) for i in range(n-1)]

# count = 0
# while set(a_in) != {0}:
#     i = max(range(0, n-2), key=lambda x: a_in[x]+a_in[x+1])
#     a_in[i]   = max(0, a_in[i] - 1)
#     a_in[i+1] = max(0, a_in[i+1] - 1)
#     count += 1
#     print(a_in)

# print(count)