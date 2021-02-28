# 9372 상근이의 여행
# https://www.acmicpc.net/problem/9372

from collections import defaultdict
import sys
from typing import Tuple


def read_two_nums() -> Tuple[int, int]:
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    return a, b


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = read_two_nums()
    answer = N - 1
    for _ in range(M):
        a, b = read_two_nums()

    print(answer)

