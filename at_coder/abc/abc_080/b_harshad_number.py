n = int(input())

print("Yes" if n % sum([int(m) for m in str(n)]) == 0 else "No")