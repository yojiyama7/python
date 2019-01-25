S = list(input())
ABCD = list(map(int, input().split(" ")))
 
for i in range(4):
    S.insert(ABCD[i]+i, '"')
 
print("".join(S))