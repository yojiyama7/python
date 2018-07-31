s = input()
n = int(input())
lr = [tuple(map(int, input().split(" "))) for i in range(n)]

for lr_i in lr:
    l, r = lr_i
    s = s[:l-1] + s[l-1:r][::-1] + s[r:]
print(s)