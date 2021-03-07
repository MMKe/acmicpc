# 베스킨라빈스 31
# https://www.acmicpc.net/problem/20004


def algorithm(n):
    num = 30
    while num > 0:
        num -= n + 1
    minimum_win_num = num + (n + 1)
    answer = n < minimum_win_num
    return answer


if __name__ == "__main__":
    A = int(input())
    for n in range(1, A + 1):
        answer = algorithm(n)
        if answer:
            print(n)
