# https://www.acmicpc.net/problem/18870

"""
좌표 압축 Coordinate compression
좌표의 범위가 너무 큰 경우, 인덱싱으로 좌표 사이의 갭을 없애는 것
충분히 큰 n, 충분히 작은 m에 대해
[-n, n] 범위에 m개의 좌표가 존재하는 경우를 생각해보자.
n은 충분히 크므로, 모든 범위를 탐색하는 것은 시간낭비이다. 
따라서 충분히 작은 m개의 좌표의 개수에 대해 좌표들을 인덱싱 하는 것이 좌표 압축 기법이다. 
"""

import sys
import heapq


def read_int() -> int:
    """
    표준 입출력으로 한 라인에 쓰여진 숫자 하나를 읽어들인다.
    """
    return int(sys.stdin.readline().strip())


N = read_int()

line = sys.stdin.readline().strip().split(" ")

nums = []
heap = []

for num in line:
    num = int(num)
    nums.append(num)
    heapq.heappush(heap, num)

order_dict = dict()
order = 0
while heap:
    num = heapq.heappop(heap)
    if num in order_dict:
        continue
    order_dict[num] = order
    order += 1

for num in nums:
    sys.stdout.write(str(order_dict[num]) + " ")

sys.stdout.flush()
