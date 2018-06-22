with open("with_tutorial_country.txt", "w", encoding="utf-8") as f: # "w" は write の意
	f.write("Japan China America England")

with open("with_tutorial_country.txt", "r", encoding="utf-8") as f:
	print(f.read()) 
	