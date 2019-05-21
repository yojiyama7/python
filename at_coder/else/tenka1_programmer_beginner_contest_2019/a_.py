A, B, C = map(int, input().split(" "))


print(["No", "Yes"][min(A, B) <= C <= max(A, B)])