# 13417 카드 문자열
# https://www.acmicpc.net/problem/13417


import sys
from collections import deque


def read_num():
    return int(sys.stdin.readline().rstrip())


T = read_num()

for _ in range(T):
    card_cnt = read_num()
    cards = deque(list(sys.stdin.readline().rstrip().split(" ")))
    s = ""

    for card in cards:
        if s == "":
            s = card
            continue

        s1 = s + card
        s2 = card + s

        s = s1 if s1 < s2 else s2

    print(s)
