a, b = [int(m) for m in input().split(" ")]

pal_sum = 0
for i in range(a, b+1):
    if str(i) == str(i)[::-1]:
        pal_sum += 1
        
print(pal_sum)