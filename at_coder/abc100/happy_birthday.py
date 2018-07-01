ab = map(int, input().split())
print("Yay!" if all([(lambda x: x <= 8)(v) for v in ab]) else ":(")