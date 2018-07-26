import os.path

# abs_path = os.path.dirname(os.path.abspath(__file__))
# def rel_path(path):
# 	return abs_path + "/" + path

contest_num = input("abcの番号: ")
contest_name = "abc_{:0>3}".format(contest_num)
if contest_num == "":
	print("入力してください")
elif os.path.isdir(contest_name):
	print("その番号はすでに存在します")
else:
	os.mkdir(contest_name)
	for c in "abcdef":
		with open("{}/{}_.py".format(contest_name, c), "w", encoding="utf-8") as f:
			f.write("")