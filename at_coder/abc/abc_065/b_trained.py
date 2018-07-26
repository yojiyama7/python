import sys

n = int(input())
a = [int(input()) for i in range(n)]

already_nums = set()
push_count = 0
i = 0
while i != 1:
    if i not in already_nums:
        already_nums.add(i)
        i = a[i]-1
        push_count += 1
    else:
        print(-1)
        sys.exit()
print(push_count)
