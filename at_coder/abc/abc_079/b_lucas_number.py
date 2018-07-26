n = int(input())

luca_nums = [2, 1]

while len(luca_nums)-1 < n:
    luca_nums.append(luca_nums[-1] + luca_nums[-2])

print(luca_nums[-1])