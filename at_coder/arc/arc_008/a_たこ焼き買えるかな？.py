N = int(input())

print(N//10*100 + (100 if N%10 >= 7 else N%10*15))