import re

s = input()

print(max([len(text) for text in re.findall("A.*Z", s)]+[0]))