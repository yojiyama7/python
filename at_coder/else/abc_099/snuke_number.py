def number_sum(num):
    digits = []
    while 0 != num:
        digits.append(num % 10)
        num //= 10
    return sum(digits)

for i in range(1, 100):
    print(i, i/number_sum(i))

# S(n) <= S(m)