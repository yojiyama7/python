from statistics import median
import math
from collections import Counter

n = int(input())
a = list(map(int, input().split(" ")))

a_counter = Counter(a)