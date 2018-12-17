A, B, N = map(int, input().split(" "))

pencil = N
mini = 0

count = 0
while pencil:
    count += pencil
    mini += pencil
    pencil = mini//A * B
    mini %= A

print(count)
    
