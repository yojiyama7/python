def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

N = int(input())

if is_prime((1+N)*(N/2)):
    print("WANWAN")
else:
    print("BOWWOW")