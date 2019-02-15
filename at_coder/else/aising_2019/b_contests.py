N = int(input())
A, B = map(int, input().split(" "))
P = list(map(int, input().split(" ")))

q_counts = [0, 0, 0]
for p in P:
    if p <= A:
        q_counts[0] += 1
    elif A+1 <= p <= B:
        q_counts[1] += 1
    elif B+1 <= p:
        q_counts[2] += 1

print(min(q_counts))
