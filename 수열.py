# 2491 수열
# https://www.acmicpc.net/problem/2491

import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split(" ")))

ascending_dp = [0] * N
ascending_dp[0] = 1

desceding_dp = [0] * N
desceding_dp[0] = 1

for idx, num in enumerate(nums):
    if idx == 0:
        continue

    before_num = nums[idx - 1]
    now_num = num

    if before_num <= now_num:
        ascending_dp[idx] = ascending_dp[idx - 1] + 1
    else:
        ascending_dp[idx] = 1

    if before_num >= now_num:
        desceding_dp[idx] = desceding_dp[idx - 1] + 1
    else:
        desceding_dp[idx] = 1

answer = 0
for dp1, dp2 in zip(ascending_dp, desceding_dp):
    answer = max(answer, max(dp1, dp2))

print(answer)
