def is_prime(n):
    if n < 2 or n&1 == 0:return False
    for i in range(3, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

N = int(input())

print("YES" if is_prime(N) else "NO")