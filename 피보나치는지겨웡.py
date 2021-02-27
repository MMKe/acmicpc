# 17175 피보나치는 지겨웡~
# https://www.acmicpc.net/problem/17175

# n | 0 1 2 3
# dp| 1 1 3 5
dp = [1, 1, 3]

n = int(input())

while len(dp) <= n:
    dp.append((sum(dp[-2:]) + 1) % 1_000_000_007)

print(dp[n] % 1_000_000_007)
