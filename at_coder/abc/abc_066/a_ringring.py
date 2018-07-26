def mins(nums, count):
    return sorted(nums)[:count]

abc = map(int, input().split(" "))

print(sum(mins(abc, 2)))