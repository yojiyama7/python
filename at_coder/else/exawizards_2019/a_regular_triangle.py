ABC = list(map(int, input().split(" ")))

print(["No", "Yes"][len(set(ABC)) == 1])