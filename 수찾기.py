# https://www.acmicpc.net/problem/1920

import sys
from typing import List


def read_int() -> int:
    """
    표준 입출력으로 숫자 하나를 받아서 리턴한다. 
    """
    import sys

    return int(sys.stdin.readline().rstrip())


def read_list_of_int() -> List[int]:
    """
    표준 입출력으로 숫자들을 읽어들여 리스트로 반환한다. 
    입력 형식은 아래와 같이 띄어쓰기로 구분된다.
    ex) n1 n2 n3 n4 ... 
    """
    import sys

    line = sys.stdin.readline().rstrip()

    return [int(num) for num in line.split(" ")]


def is_exist(numbers: List[int], target: int) -> bool:
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return True

        elif numbers[mid] < target:
            left = mid + 1
            continue
        else:
            right = mid - 1
            continue

    return False


n = read_int()
nums = read_list_of_int()
m = read_int()
targets = read_list_of_int()

nums.sort()

answers = []
for target in targets:
    answer = is_exist(nums, target)

    answer = 1 if answer else 0

    sys.stdout.write(str(answer) + "\n")

sys.stdout.flush()
