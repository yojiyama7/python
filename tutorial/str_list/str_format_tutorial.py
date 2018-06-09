str_list = ["text", "python", "discord", "connect", "clock"]
x = max([len(s) for s in str_list])

for s in str_list:
    print("{: >{}}".format(s, x))
