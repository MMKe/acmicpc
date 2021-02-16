import sys
from collections import deque

_ = int(sys.stdin.readline())

distances = map(int, sys.stdin.readline().rstrip().split(" "))
prices = map(int, sys.stdin.readline().rstrip().split(" "))

distances = deque(distances)
prices = deque(prices)

now_price = prices.popleft()
answer = 0

while prices:
    next_price = prices.popleft()

    if now_price <= next_price:
        answer += now_price * distances.popleft()
    else:
        answer += now_price * distances.popleft()
        now_price = next_price

print(answer)
