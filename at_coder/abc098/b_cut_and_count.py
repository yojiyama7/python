def same_count(str_list):
    standard_str = min(str_list, key=lambda x: len(x))
    return [all([c in str_ for str_ in str_list]) for c in set(standard_str)].count(True)

n = int(input())
s = input()

print(max([same_count([s[:i+1], s[i+1:]]) for i in range(n)]+[0]))