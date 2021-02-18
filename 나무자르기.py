# https://www.acmicpc.net/problem/2805

from typing import List, Callable


def read_int() -> int:
    """
    표준 입출력으로 한 라인에 쓰여진 숫자 하나를 읽어들인다.
    """
    import sys

    return int(sys.stdin.readline().strip())


def read_list(func: Callable = None) -> List:
    """
    표준 입출력으로 한 라인을 읽어들이고, 주어진 func 함수로 매핑하여 리스트로 반환한다.
    라인의 요소들은 space로 구분되어야 한다.
    """
    import sys

    return list(map(func, sys.stdin.readline().strip().split(" ")))


def cut_trees(trees, height):
    """
    height 높이에서 trees들을 잘랐을 때 얻을 수 있는 목재들의 길이의 합을 반환한다.
    """
    answer = 0

    for tree in trees:
        answer += (tree - height) if tree >= height else 0

    return answer


N, M = read_list(int)
trees = read_list(int)

left = 0
right = max(trees)
answer = 0

while left <= right:
    mid = (left + right) // 2

    cutted_trees_length = cut_trees(trees, mid)

    if cutted_trees_length < M:  # 더 많이 잘라야 하는 경우,
        right = mid - 1
        continue
    else:
        answer = max(mid, answer)
        left = mid + 1

print(answer)

