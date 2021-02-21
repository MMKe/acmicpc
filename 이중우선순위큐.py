# https://www.acmicpc.net/problem/7662

import sys
import heapq


def read_int():
    return int(sys.stdin.readline().rstrip())


def read_line(func):
    return list(map(func, sys.stdin.readline().rstrip().split(" ")))


def reverse_heap(heap):
    result_heap = []

    for num in heap:
        heapq.heappush(result_heap, num * -1)

    return result_heap


def clean_heap(heap, num_deleted):
    while heap:
        _, num_idx = heap[0]
        if num_deleted[num_idx]:
            heapq.heappop(heap)
        else:
            break


def solution():
    N = read_int()

    num_deleted = [False] * N
    min_heap = []
    max_heap = []

    for idx in range(N):
        command, num = read_line(str)
        num = int(num)

        if command == "I":
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (num * -1, idx))
            continue
        else:  # command == 'D'
            if num == -1:  # 최솟값 삭제
                clean_heap(min_heap, num_deleted)
                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    num_deleted[idx] = True
            else:  # 최댓값 삭제
                clean_heap(max_heap, num_deleted)
                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    num_deleted[idx] = True

    clean_heap(max_heap, num_deleted)
    clean_heap(min_heap, num_deleted)

    if min_heap and max_heap:
        result = []

        max_num = heapq.heappop(max_heap)[0] * -1
        min_num = heapq.heappop(min_heap)[0]

        result.append(max_num)
        result.append(min_num)

        return " ".join(map(str, result))

    return "EMPTY"


T = read_int()

for _ in range(T):
    print(solution())
