# 4779 칸토어 집합
# https://www.acmicpc.net/problem/4779

from typing import List


def divide_and_conquer(arr: List[str], start=None, end=None):
    if start == None and end == None:
        start = 0
        end = len(arr)

    if start == end - 1:
        return

    offset = (end - start) // 3

    # start                 ~ start + offset
    # start + offset        ~ start + 2 * offset
    # start + 2 * offset    ~ end
    arr[start + offset : start + 2 * offset] = [" "] * offset

    divide_and_conquer(arr, start, start + offset)
    divide_and_conquer(arr, start + 2 * offset, end)


import sys

while line := sys.stdin.readline():
    N = int(line)
    arr = ["-"] * 3 ** N

    divide_and_conquer(arr)

    print("".join(arr))
