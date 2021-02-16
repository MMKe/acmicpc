# https://www.acmicpc.net/problem/4949

import sys


def read_line():
    line = sys.stdin.readline().rstrip()

    if line == ".":
        return False

    return line[:-1]


def is_balanced(s):
    brackets = ["(", ")", "[", "]"]

    stack = []

    for c in s:
        if c not in brackets:
            continue

        if c == "(" or c == "[":
            stack.append(c)
            continue

        if c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)

            continue

        if c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)

            continue

    return "no" if stack else "yes"


while True:
    s = read_line()

    if s is False:
        break

    check = is_balanced(s)
    print(check)
