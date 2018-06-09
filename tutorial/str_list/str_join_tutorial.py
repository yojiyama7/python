words = ["place", "And", "pop", "TEXT", "TokeN", "ok", "jacK"]

for i, word in enumerate(words):
    words[i] = word.lower() if i % 2 else word.upper()

print(words)
print("".join(words))
