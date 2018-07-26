def two_count(num):
    count = 0
    while num % 2 == 0:
        count += 1
        num //= 2
    return count

n = int(input())

n_two_count = [two_count(n_i) for n_i in range(1, n+1)]
print(n_two_count.index(max(n_two_count))+1)