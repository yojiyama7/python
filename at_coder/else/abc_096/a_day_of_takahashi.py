month, day = [int(i) for i in input().split(" ")]

if month <= day:
    takahashi_day_num = month
else:
    takahashi_day_num = month - 1

print(takahashi_day_num)