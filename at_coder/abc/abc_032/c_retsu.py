# わからん TLE

n, k = map(int, input().split(" "))
s = [int(input()) for _ in range(n)]

if 0 in s:
    print(n)
    exit()

products = [1]
for s_i in s:
    products.append(products[-1]*s_i)

a, b, max_len = 0, 0, 0
while b <= n:
    if products[b] // products[a] <= k:
        if b-a > max_len:
            max_len = b-a
        b += 1
    else:
        a += 1
    b = a if b < a else b

print(max_len)
