# https://www.acmicpc.net/problem/1620

import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

pokemon_list = []  # 숫자로 찾을 때 사용
pokemon_dict = dict()  # 이름으로 찾을 때 사용

pokemon_list.append("dummy")

for i in range(n):
    pokemon = sys.stdin.readline().rstrip()

    pokemon_list.append(pokemon)
    pokemon_dict[pokemon] = i + 1

for _ in range(m):
    find = sys.stdin.readline().rstrip()

    if find.isalpha():  # 이름으로 찾는 경우
        print(pokemon_dict[find])
    elif find.isdigit():  # 번호로 찾는 경우
        print(pokemon_list[int(find)])
