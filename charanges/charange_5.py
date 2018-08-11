### 01 ###

for c in "カミュ":
	print(c)

### 02 ###

print("私は昨日{}を書いて、{}に送った！".format(input(), input()))

### 03 ###

print("aldous Huxley was born in 1894.".capitalize())

### 04 ###

print("どこで？ だれが？ いつ？".split(" "))

### 05 ###

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
print(" ".join(words[:-1]) + words[-1])

### 06 ###

print("A screaming somes across the sky.".replace("s", "$"))

### 07 ###

print("Hemingway".find("m"))

### 08 ###

print("I'm sorry")

### 09 ###

print("three" + "three" + "three")
print("three" * 3)

### 10 ###

text = "四月の晴れた寒い日で、時計がどれも十三時を打っていた"
print(text[:text.find("、")])