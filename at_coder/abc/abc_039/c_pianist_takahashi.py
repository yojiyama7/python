s = input()

do_to_si = "WBWBWWBWBWBW"
n = (s[:12]*2).rfind(do_to_si)
key_boards = ["Do", None, "Re", None, "Mi", "Fa", None, "So", None, "La", None, "Si", None]
print(key_boards[~n])
