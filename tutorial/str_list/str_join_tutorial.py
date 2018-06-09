words = ["place", "And", "pop", "TEXT", "TokeN", "ok", "jacK"]

changed_words = []
for i, word in enumerate(words):
    changed_words.append(word.lower() if i % 2 else word.upper())

print(changed_words)
print("".join(changed_words))
