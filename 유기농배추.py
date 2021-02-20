# https://www.acmicpc.net/problem/1012

import sys
from collections import deque
from typing import Callable, List
from pprint import pprint


def read_int() -> int:
    """표준 입력으로 한 줄을 읽고 숫자로 변환하여 반환"""
    return int(sys.stdin.readline().rstrip())


def read_line(func: Callable = None) -> List[int]:
    """
    표준 입력으로 라인을 읽어서 func으로 매핑하여 반환
    func는 필수 파라미터이며, 라인의 입력값은 ' '으로 구분되어 있어야 한다.
    """
    return map(func, sys.stdin.readline().rstrip().split(" "))


def bfs(board: List[List[int]], i: int, j: int):
    def is_one(i: int, j: int) -> bool:
        if i < 0 or i > len(board) - 1:
            return False

        if j < 0 or j > len(board[i]) - 1:
            return False

        return board[i][j] == 1

    queue = deque()
    queue.append((i, j))
    board[i][j] = 0

    while queue:
        i, j = queue.popleft()

        if is_one(i - 1, j) == 1:
            queue.append((i - 1, j))
            board[i - 1][j] = 0
        if is_one(i + 1, j) == 1:
            queue.append((i + 1, j))
            board[i + 1][j] = 0
        if is_one(i, j - 1) == 1:
            queue.append((i, j - 1))
            board[i][j - 1] = 0
        if is_one(i, j + 1) == 1:
            queue.append((i, j + 1))
            board[i][j + 1] = 0

    return


def solution():
    M, N, K = read_line(int)

    board = [[0] * M for _ in range(N)]
    cabbage_points = []

    for _ in range(K):
        j, i = read_line(int)
        cabbage_points.append((i, j))
        board[i][j] = 1

    answer = 0

    for i, j in cabbage_points:
        if board[i][j] == 1:
            answer += 1
            bfs(board, i, j)

    return answer


T = read_int()

for _ in range(T):
    answer = solution()
    sys.stdout.write(str(answer) + "\n")

sys.stdout.flush()
