def count_two(num):
    count = 0
    while num % 2 == 0:
        count += 1
        num //= 2
    return count

n = int(input())
a = [int(m) for m in input().split(" ")]

print(min([count_two(a_i) for a_i in a]))