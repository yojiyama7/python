import time

COUNT = 10000
NUM = 342407328

start = time.time()

for i in range(COUNT):
    digits = []
    n = NUM
    while 0 < n:
        digits.append(n % 10)
        n //= 10
print(digits)

while_time = time.time() - start

start = time.time()

for i in range(COUNT):
    digits = []
    n = NUM
    digits = list(map(int, str(n)))
    # digits = map(int, str(n))
print(digits)

str_time = time.time() - start

print(while_time, str_time, while_time/str_time)