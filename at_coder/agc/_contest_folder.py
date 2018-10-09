import os.path

CONTEST_NAME_FORMAT = "agc_{:0>3}"
FILE_NAME_FORMAT = "{}_.py"
FILE_NAMES = "abcdef"
DEFAULT_TEXT = ""

def input_contest_name(num):
	name = CONTEST_NAME_FORMAT.format(num)
	if num == "":
		print("入力してください")		
	elif os.path.isdir(name):
		print("その番号はすでに存在します")
	else:
		return name
def mk_abc_dir(contest_name):
	os.mkdir(contest_name)
	for file_name in FILE_NAMES:
		with open("{}/".format(contest_name) + FILE_NAME_FORMAT.format(file_name), "w", encoding="utf-8") as f:
			f.write(DEFAULT_TEXT)
def create_folder(num):
	name = input_contest_name(num)
	if name:
		mk_abc_dir(name)

create_folder(input("abcの番号: "))
