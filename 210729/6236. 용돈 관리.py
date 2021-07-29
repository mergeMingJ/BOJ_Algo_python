import sys
sys.stdin = open('input/6236.txt', 'r')

N, M = map(int, input().split())
costs = []
for _ in range(N):
    costs.append(int(input()))
max_value = max(costs)
min_value = min(costs)
value = max_value
day = 0
