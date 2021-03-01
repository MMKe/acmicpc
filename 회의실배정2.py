# 19621 회의실 배정2
# https://www.acmicpc.net/problem/19621

import sys


def read_num():
    return int(sys.stdin.readline().rstrip())


def read_nums():
    return list(map(int, sys.stdin.readline().rstrip().split(" ")))


N = read_num()
dp = [0]
nums = [0]
for _ in range(N):
    a, b, num = read_nums()
    nums.append(num)

for idx, num in enumerate(nums):
    if idx == 0:
        continue
    if idx <= 2:
        dp.append(num)
        continue

    dp.append(num + max(dp[idx - 2], dp[idx - 3]))

answer = 0
for ans in dp:
    answer = max(answer, ans)
print(answer)
