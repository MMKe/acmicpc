# https://www.acmicpc.net/problem/10866

import sys
from collections import deque


def read_int():
    """
    표준 입력으로 한줄을 읽어서 int로 반환한다.
    """
    return int(sys.stdin.readline().rstrip())


N = read_int()

dq = deque()
for _ in range(N):
    line = sys.stdin.readline().rstrip()

    if line.startswith("push_back"):
        _, X = line.split(" ")
        dq.append(X)
    elif line.startswith("push_front"):
        _, X = line.split(" ")
        dq.appendleft(X)
    elif line == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif line == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif line == "size":
        print(len(dq))
    elif line == "empty":
        print(1 if len(dq) == 0 else 0)
    elif line == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif line == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
        
    

