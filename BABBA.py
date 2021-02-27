# 9625 BABBA
# https://www.acmicpc.net/problem/9625

N = int(input())

answer = {
    "a": 1,
    "b": 0,
}

for _ in range(N):
    a, b = answer["a"], answer["b"]
    answer = {
        "a": 0,
        "b": 0,
    }
    answer["b"] += a  # a는 B로 바뀐다
    answer["a"] += b  # b는 A와 B로 바뀐다
    answer["b"] += b  # b는 A와 B로 바뀐다

print("%d %d" % (answer["a"], answer["b"]))
