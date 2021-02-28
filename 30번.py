# 13116 30번
# https://www.acmicpc.net/problem/13116

import sys
from typing import Tuple


def read_two_nums() -> Tuple[int, int]:
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    return a, b


def get_depth(num):
    import math

    return int(math.log2(num))


def get_parent(num):
    return num // 2


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a, b = read_two_nums()

    # 두 수의 깊이(depth)를 구한다
    a_depth = get_depth(a)
    b_depth = get_depth(b)

    # 깊이를 같게 맞춘다
    while a_depth != b_depth:
        if a_depth > b_depth:
            a = get_parent(a)
            a_depth -= 1
        else:
            b = get_parent(b)
            b_depth -= 1

    # 두 수가 같아질 때까지 부모로 거슬러 올라간다
    while a != b:
        a = get_parent(a)
        b = get_parent(b)

    print(10 * a)