x = input()

while x:
    index = sum([len(word) if word==x[:len(word)] else 0 for word in ("ch", "o", "k", "u")])
    if index == 0:
        print("NO")
        exit()
    x = x[index:]
print("YES")