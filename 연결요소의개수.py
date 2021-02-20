# https://www.acmicpc.net/problem/11724

import sys
from typing import List, Callable, Dict
from collections import defaultdict


def read_list(func: Callable = None) -> List:
    """
    표준 입출력으로 한 라인을 읽어들이고, 주어진 func 함수로 매핑하여 리스트로 반환한다.
    라인의 요소들은 space로 구분되어야 한다.
    """
    return list(map(func, sys.stdin.readline().strip().split(" ")))


def dfs(graph: Dict, start_node: int, visited: List[bool]):
    connected_nodes = graph[start_node]

    for connected_node in connected_nodes:
        if visited[connected_node] == False:
            visited[connected_node] = True
            dfs(graph, connected_node, visited)


sys.setrecursionlimit(2000)  # 기본값으로 하면 RecursionError 발생

N, M = read_list(int)

graph = defaultdict(list)
for _ in range(M):
    node1, node2 = read_list(int)

    # 노드의 번호를 0-index로 수정한다.
    node1 -= 1
    node2 -= 1

    graph[node1].append(node2)
    graph[node2].append(node1)

answer = 0
visited = [False] * N

for node in range(N):
    if visited[node] == False:
        visited[node] = True
        answer += 1
        dfs(graph, node, visited)

print(answer)
