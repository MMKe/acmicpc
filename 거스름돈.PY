# 14916 거스름돈

n = int(input())

a, b = divmod(n, 5)

if b % 2 == 0:
    b = b // 2
else:
    a -= 1
    b = (b + 5) // 2

if a == -1:
    print(-1)
else:
    print(a + b)
