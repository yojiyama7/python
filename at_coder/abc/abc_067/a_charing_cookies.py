a, b = map(int, input().split(" "))

print("Possible" if any(map(lambda x: x%3 == 0, (a, b, a+b))) else "Impossible")