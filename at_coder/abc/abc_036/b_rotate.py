n = int(input())
s = [input() for i in range(n)]

[print("".join(line)[::-1]) for line in zip(*s)]