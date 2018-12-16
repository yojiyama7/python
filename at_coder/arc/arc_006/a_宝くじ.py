E = set(map(int, input().split(" ")))
B = int(input())
L = set(map(int, input().split(" ")))

match, bonus = len(E&L), B in L
if match == 6:
    print(1)
elif (match, bonus) == (5, 1):
    print(2)
elif 3 <= match <= 5:
    print(8-match)
else:
    print(0)