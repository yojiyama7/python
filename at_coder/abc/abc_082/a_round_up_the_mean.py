def round_up(num):
    if num % 1 == 0:
        return int(num)
    return int(num) + 1

ab = [int(m) for m in input().split(" ")]

print(round_up(sum(ab) / 2))