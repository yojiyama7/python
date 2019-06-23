S = input()

print(["Bad", "Good"][all(S[i] != S[i+1] for i in range(3))])