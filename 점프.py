# 1890 점프
# https://www.acmicpc.net/problem/1890

import sys
from collections import defaultdict


def read_num():
    return int(sys.stdin.readline().rstrip())


def read_nums():
    return list(map(int, sys.stdin.readline().rstrip().split(" ")))


def dfs(board, dp, r, c):
    try:
        answer = dp[r][c]
        return answer
    except (KeyError, IndexError):
        pass

    N = len(board)
    maximum_index = N - 1
    num = board[r][c]

    if r == maximum_index and c == maximum_index:
        return 1

    if num == 0:
        return 0

    right, down = 0, 0
    if c + num > maximum_index:
        pass
    else:
        right = dfs(board, dp, r, c + num)

    if r + num > maximum_index:
        pass
    else:
        down = dfs(board, dp, r + num, c)

    dp[r][c] = right + down

    return dp[r][c]


N = read_num()

board = []
for _ in range(N):
    board.append(read_nums())

dp = defaultdict(dict)

dfs(board, dp, 0, 0)

print(dp[0][0])

