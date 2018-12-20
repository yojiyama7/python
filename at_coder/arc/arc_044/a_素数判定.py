def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3 or n == 5:
        return True
    for m in [2, 3, 5]:
        if n%m == 0:
            return False
    return True

N = int(input())

print("Prime" if is_prime(N) else "Not Prime")