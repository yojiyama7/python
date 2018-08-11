### 01 ###

movies = [
	"ウォーキング・デッド",
	"アントラージュ",
	"ザ・ソプラノズ",
	"ヴァンパイア",
	"ダイアリーズ"
]
for movie in movies:
	print(movie)

### 02 ###

for i in range(25, 51):
	print(i)

### 03 ###

for i, movie in enumerate(movies):
	print(i, movie)

### 04 ###

while True:
	input_text = input()
	if input_text == "q":
		print("終了します")
		break
	try:
		num = int(input_text)	
	except:
		print("数字を入力するか、qで終了します")
		continue
	if num in [1, 2, 3]:
		print("正解")
	else:
		print("不正解")
	break

### 05 ###

divs = []
for x in [8, 19, 138, 4]:
	for y in [9, 1, 33, 83]:
		divs.append(x*y)
print(divs)