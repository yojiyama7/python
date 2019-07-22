L, R = map(int, input().split(" "))

if R-L >= 2019:
    print(0)
    exit()

l = [i%2019 for i in range(L, R+1)]
min_num = 10**18
for i in range(len(l)):
    for j in range(i+1, len(l)):
        m = (l[i]*l[j])%2019
        if m < min_num:
            min_num = m

print(min_num)