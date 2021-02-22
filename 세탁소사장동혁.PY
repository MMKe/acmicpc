import sys

write = sys.stdout.write

T = int(input())

for _ in range(T):
    total = int(input())

    cnt = 0
    while total >= 25:
        total -= 25
        cnt += 1
    write(str(cnt) + " ")

    cnt = 0
    while total >= 10:
        total -= 10
        cnt += 1
    write(str(cnt) + " ")

    cnt = 0
    while total >= 5:
        total -= 5
        cnt += 1
    write(str(cnt) + " ")

    cnt = 0
    while total >= 1:
        total -= 1
        cnt += 1
    write(str(cnt) + " ")

    write("\n")
