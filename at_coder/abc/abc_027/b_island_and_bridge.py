n = int(input())
a = tuple(map(int, input().split(" ")))

# リスト使ったほうがいい
if sum(a) % len(a) == 0:
    group_count = 0
    island_count = 0
    person_sum = 0
    ave = sum(a) // len(a)
    for a_i in a:
        person_sum += a_i
        island_count += 1
        if person_sum % island_count == 0 and person_sum // island_count == ave:
            group_count += 1
            person_sum = 0
            island_count = 0
    print(len(a) - group_count)
else:
    print(-1)