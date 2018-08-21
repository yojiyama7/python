s = input()

print(sum(["0" not in item for item in s.split("+")]))