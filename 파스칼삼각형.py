# 파스칼 삼각형 15489
# https://cocoon1787.tistory.com/412

dp = []
for i in range(31):
    dp.append([0] * 31)

for i in range(1, 31):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]


R, C, W = map(int, input().split(" "))

answer = 0
for i in range(W):
    for j in range(i + 1):
        answer += dp[R + i][C + j]

print(answer)
