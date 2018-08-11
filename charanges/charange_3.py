### 01 ###

def square(n):
	"""
	type:
		n: int, float
	"""
	return n ** 2

### 02 ###

def printy(text):
	"""
	type:
		text: str
	"""
	print(text)

### 03 ###

def abcde(a, b, c, d=0, e=0):
	"""
	type:
		a, b, c, d, e: int, float
	"""
	return a + b + c + d + e

### 04 ###

def half(n):
	"""
	type:
		n: int
	"""
	return n // 2

def four(n):
	"""
	type:
		n: int
	"""
	return n * 4

x = half(34)
print(four(x))

### 05 ###

def str_to_float(text):
	"""
	type:
		text: str
	"""
	try:
		return float(text)
	except:
		print("その文字列はfloatにできません")

print(str_to_float("5.3"))
print(str_to_float("abc"))

### 06 ###

# doc string