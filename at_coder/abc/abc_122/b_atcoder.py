import re

S = input()

print(max(0, *map(len, re.findall("[AGCT]*", S))))