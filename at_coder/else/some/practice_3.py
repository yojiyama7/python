# def two_count(x):
# 	if x % 2 == 0:
# 		return 1 + two_count(x//2)
# 	else:
# 		return 0

# n = int(input())
# n_list = [int(n) for n in input().split(" ")]

# n_two_count_list = [two_count(n) for n in n_list]

# print(min(n_two_count_list))

def is_divisible(x):
    if x % 2 == 0:
        return True
    return False

num = int(input())
count = 0
lis = [int(n) for n in input().split()]

while all([is_divisible(n) for n in lis]):
    count += 1
    lis = [n//2 for n in lis]

print(count)