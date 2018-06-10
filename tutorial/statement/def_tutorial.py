def words_len(words):
    lens = []
    for word in words:
        lens.append(len(word))
    return lens

def jagged_text(text):
    jagged_str = ""
    for i, c in enumerate(text):
        if i % 2 == 0:
            jagged_str += c.upper()
        else:
            jagged_str += c.lower()
    return jagged_str

words = ["for", "if", "enumerate"]
print(words_len(words))

# >>> [3, 2, 9]

print(jagged_text("Floccinaucinihilipilification"))

# >>> FlOcCiNaUcInIhIlIpIlIfIcAtIoN
