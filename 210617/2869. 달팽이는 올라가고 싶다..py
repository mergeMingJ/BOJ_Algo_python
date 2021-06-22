import math
import sys
sys.stdin = open('input/2869.txt', 'r')

T = int(input())

for t in range(T):
    A, B, V = list(map(int, input().split()))

    # 하루: A, 도달 되지 않았을 경우 A-B
    # 최소 몇일 걸리는지 : 도달값 - A / 도달되지 않았을 경우 올라가는 높이
    max_value = math.ceil((V-A)/(A-B))

    # A만 올라가는 경우도 계산 해야되서 +1 해줌
    day = max_value+1
    # 현재 높이
    current = V-A

    while current < V:
        current += A
        if current >= V:
            break;
        else:
            current-=B
            day+=1

    print(t+1, day)

