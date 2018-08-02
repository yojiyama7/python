n = int(input())
a = list(map(int, input().split(" ")))

a = [0] + a + [0]
a_walks = [abs(a[i+1]-a[i]) for i in range(n+1)]
