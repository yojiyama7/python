S = int(input())

n = S
a = {S}
for i in range(1, 10**6+1):
    if n%2==0:
        n = n//2
    else:
        n = 3*n+1
    
    if n in a:
        print(i+1)
        exit()
    else:
        a.add(n)
    