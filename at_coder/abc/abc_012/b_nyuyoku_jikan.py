n = int(input())

print(":".join([str(m).rjust(2, '0') for m in (n//3600, n//60%60, n%60)]))