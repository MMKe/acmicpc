# https://www.acmicpc.net/problem/5430

import sys
from collections import deque


def read_line(func=None):
    if func is None:
        return sys.stdin.readline().rstrip()
    else:
        return func(sys.stdin.readline().rstrip())


N = read_line(int)

for _ in range(N):
    commands = read_line(str)
    length = read_line(int)
    numbers = read_line(str)

    numbers = numbers[1:-1]  # 양 끝의 괄호 제거
    if not numbers:
        numbers = []
    else:
        numbers = [int(number) for number in numbers.split(",")]  # 파싱하여 리스트로 변환

    dq = deque(numbers)
    is_right = True  # True일때 popleft() 호출한다.

    try:
        for command in commands:
            if command == "R":
                is_right = not is_right
                continue

            if command == "D":
                if is_right:  # True일때 popleft() 호출한다.
                    dq.popleft()
                else:
                    dq.pop()

        dq = [str(n) for n in dq]
        if is_right:
            pass
        else:
            dq.reverse()

        print("[" + ",".join(dq) + "]")
    except IndexError:
        print("error")

