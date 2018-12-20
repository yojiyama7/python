S = input().split(" ")

print(" ".join({"Left": "<", "Right": ">", "AtCoder": "A"}[s] for s in S))