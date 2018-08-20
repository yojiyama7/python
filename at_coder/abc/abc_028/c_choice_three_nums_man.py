from itertools import combinations

abcde = tuple(map(int, input().split(" ")))

print(sorted(set(sum(nums) for nums in combinations(abcde, 3)), reverse=True)[2])