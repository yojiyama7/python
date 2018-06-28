n = int(input())
s = input().split(" ")

s_type_len = len(set(s))

if s_type_len == 3:
    print("Three")
elif s_type_len == 4:
    print("Four")