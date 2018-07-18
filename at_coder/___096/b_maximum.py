abc = [int(i) for i in input().split(" ")]
k = int(input())

abc_max = max(abc)
abc.remove(abc_max)
k_to_abc_max = abc_max * (2 ** k)
board_sum = sum(abc + [k_to_abc_max])

print(board_sum)

