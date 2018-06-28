# N K
# A1 A2 … AN

import sys

n, k = map(int, sys.stdin.readline().split())

print((n-2) // (k-1) + 1)