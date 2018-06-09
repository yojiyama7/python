words = ["text", "python", "discord", "connect", "clock"]
x = max([len(s) for s in words])

for word in words:
    print("{: >{}}".format(word.capitalize(), x))
