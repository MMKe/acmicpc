# 3184 양
# https://www.acmicpc.net/problem/3184


import sys
from collections import deque


def read_nums():
    return list(map(int, sys.stdin.readline().rstrip().split(" ")))


def can_go_left(yard, point):
    r, c = point

    if c == 0:
        return False
    if yard[r][c - 1] == "#":
        return False
    return True


def can_go_right(yard, point):
    r, c = point

    row_length = len(yard[0])
    row_maximum_index = row_length - 1

    if c == row_maximum_index:
        return False
    if yard[r][c + 1] == "#":
        return False
    return True


def can_go_up(yard, point):
    r, c = point

    if r == 0:
        return False
    if yard[r - 1][c] == "#":
        return False
    return True


def can_go_down(yard, point):
    r, c = point

    col_length = len(yard[0])
    col_maximum_index = col_length - 1

    if r == col_maximum_index:
        return False
    if yard[r + 1][c] == "#":
        return False
    return True


R, C = read_nums()

yard = []
sheeps = 0
wolves = 0
wolf_points = []
for r in range(R):
    row = sys.stdin.readline().rstrip()

    splited_row = []
    for c, ele in enumerate(row):
        if ele == "o":  # 양
            sheeps += 1
        if ele == "v":  # 늑대
            wolves += 1
            wolf_points.append((r, c))

        splited_row.append(ele)

    yard.append(splited_row)


for wolf_point in wolf_points:
    queue = deque()
    queue.append(wolf_point)
    wolf_r, wolf_c = wolf_point
    if yard[wolf_r][wolf_c] == "#":  # 이미 체크된 영역의 wolf_point인 경우 생략한다.
        continue
    else:
        yard[wolf_r][wolf_c] = "#"

    wolf_in_space = 1
    sheep_in_space = 0
    while queue:
        now_point = queue.popleft()
        point_r, point_c = now_point

        if can_go_left(yard, now_point):
            if yard[point_r][point_c - 1] == "o":
                sheep_in_space += 1
            if yard[point_r][point_c - 1] == "v":
                wolf_in_space += 1

            yard[point_r][point_c - 1] = "#"
            queue.append((point_r, point_c - 1))
        if can_go_right(yard, now_point):
            if yard[point_r][point_c + 1] == "o":
                sheep_in_space += 1
            if yard[point_r][point_c + 1] == "v":
                wolf_in_space += 1

            yard[point_r][point_c + 1] = "#"
            queue.append((point_r, point_c + 1))
        if can_go_up(yard, now_point):
            if yard[point_r - 1][point_c] == "o":
                sheep_in_space += 1
            if yard[point_r - 1][point_c] == "v":
                wolf_in_space += 1

            yard[point_r - 1][point_c] = "#"
            queue.append((point_r - 1, point_c))
        if can_go_down(yard, now_point):
            if yard[point_r + 1][point_c] == "o":
                sheep_in_space += 1
            if yard[point_r + 1][point_c] == "v":
                wolf_in_space += 1

            yard[point_r + 1][point_c] = "#"
            queue.append((point_r + 1, point_c))

    if sheep_in_space > wolf_in_space:
        wolves -= wolf_in_space
    else:
        sheeps -= sheep_in_space

print("%d %d" % (sheeps, wolves))

