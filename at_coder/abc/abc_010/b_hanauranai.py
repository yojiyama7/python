n = int(input())
a = tuple(map(int, input().split(" ")))

sum_num = 0
for a_i in a:
    count = 0
    while a_i%2==0 or a_i%3==2:
        a_i -= 1
        count += 1
    sum_num += count

print(sum_num)