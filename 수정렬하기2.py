# https://www.acmicpc.net/problem/2751

import sys
import heapq


def read_int():
    i = sys.stdin.readline()

    return int(i)


N = read_int()

h = []

for _ in range(N):
    n = read_int()
    heapq.heappush(h, n)

while h:
    n = heapq.heappop(h)
    print(n)
