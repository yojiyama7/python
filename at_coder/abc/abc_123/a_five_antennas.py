abcde = [int(input()) for _ in range(5)]
k = int(input())

if k < abcde[-1] - abcde[0]:
    print(":(")
else:
    print("Yay!")