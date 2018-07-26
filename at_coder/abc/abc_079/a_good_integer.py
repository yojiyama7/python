n_str = input()

if len(set(n_str[:3])) == 1 or len(set(n_str[1:])) == 1:
    print("Yes")
else:
    print("No")