N, A, B = map(int, input().split(" "))

print(max(0, (A+B*(N-1))-(B+A*(N-1))+1))