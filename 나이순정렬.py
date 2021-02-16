# https://www.acmicpc.net/problem/10814

import sys
import heapq


def read_int() -> int:
    i = sys.stdin.readline()

    return int(i)


def parse_line() -> tuple:
    line: str = sys.stdin.readline()

    line = line.rstrip()

    age, name = line.split(" ")

    return int(age), name


N = read_int()
h = []

for i in range(N):
    age, name = parse_line()
    heapq.heappush(h, (age, i, name))  # 나이, 가입순서 순으로 오름차순 정렬이 된다.

while h:
    age, _, name = heapq.heappop(h)

    print(age, name)

