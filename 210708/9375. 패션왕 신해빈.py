import sys
from itertools import combinations
sys.stdin = open('input/9375.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    style_item = []
    total = {}
    if N == 0:
        print(0)
    else:
        for n in range(N):
            name, category = input().split()
            if category in total:
                total[category] += 1
            else:
                total[category] = 0
                total[category] += 1
        items = list(total.values())

        total_cnt = 0

        for i in range(1, len(items)+1):
            pass
        #   다시 한번 생각

        print(total_cnt)



