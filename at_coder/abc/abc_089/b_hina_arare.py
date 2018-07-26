n = int(input())
s = input().split(" ")

print({3: "Three", 4: "Four"}[len(set(s))])