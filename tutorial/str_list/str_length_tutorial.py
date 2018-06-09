str_list = ["string", "integer", "list", "bool", "A", "brainf*cker"]

for s in str_list:
    print("{s}: {len_s}".format(s=s, len_s=len(s)))