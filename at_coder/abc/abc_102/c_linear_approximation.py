import statistics

n = int(input())
a = [int(n) for n in input().split(" ")]

sub_a = [a_n - i - 1 for i, a_n in enumerate(a)]
median = statistics.median(sub_a)
print(int(sum([abs(sub_a_n-median) for sub_a_n in sub_a])))