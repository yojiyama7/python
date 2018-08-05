# よくわかっとらん
n = int(input())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
counts = [0]*(n+1)
for i in range(2, n+1):
    for prime in primes:
        while i % prime == 0:
            counts[prime] += 1
            i //= prime
    if i > 1:
        counts[i] += 1

print(counts)
score = 1
for count in counts:
    score = (score * (count + 1)) % (10**9+7)
print(score)
