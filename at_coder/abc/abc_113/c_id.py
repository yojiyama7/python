from itertools import groupby

n, m = map(int, input().split(" "))
py = [list(map(int, input().split(" "))) for _ in range(m)]

py = [py_i + [i] for i, py_i in enumerate(py)]
py_ = []
for key, group in groupby(sorted(py, key=lambda x: x[0]), lambda x: x[0]):
	for i, city in enumerate(sorted(group, key=lambda x: x[1])):
		py_.append(city + [i+1])

py = sorted(py_, key=lambda x: x[2])

for py_i in py:
	print(str(py_i[0]).zfill(6) + str(py_i[3]).zfill(6))

