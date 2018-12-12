# わがらんぞー
# いけたぞー適当だぞー

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

N = int(input())

p = [0]*(N+1)

for i in range(2, N+1):
    for j in range(2, i+1):
        if is_prime(j) == False:
            continue
        while i%j==0:
            i //= j
            p[j] += 1
        if i == 1:
            break

r = 1
for q in p:
    r = r * (q+1)
print(r%(10**9+7))


################################
#-------------------------------
################################

# よくわかっとらん
# n = int(input())
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# counts = [0]*(n+1)
# for i in range(2, n+1):
#     for prime in primes:
#         while i % prime == 0:
#             counts[prime] += 1
#             i //= prime
#     if i > 1:
#         counts[i] += 1

# print(counts)
# score = 1
# for count in counts:
#     score = (score * (count + 1)) % (10**9+7)
# print(score)
