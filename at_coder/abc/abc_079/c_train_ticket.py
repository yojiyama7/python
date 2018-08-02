a, b, c, d = input()

for x in "+-":
	for y in "+-":
		for z in "+-":
			formula = a +x+ b +y+ c +z+ d
			if eval(formula) == 7:
				print(formula + "=7")
				exit()