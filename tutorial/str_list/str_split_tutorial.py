texts = ["word", "kidai,is,shit", "split,tepodon"]

words = ",".join(texts).split(",")

print(words)

# import itertools
#
# texts = ["word", "kidai,is,shit", "split,tepodon"]
#
# words = list(itertools.chain(*[text.split(",") for text in texts]))
#
# print(words)
