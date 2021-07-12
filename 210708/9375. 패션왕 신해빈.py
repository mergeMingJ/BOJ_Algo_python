import sys
sys.stdin = open('input/9375.txt', 'r')


# { a: 2, b:3, c:4 }
# ans = (2+1)*(3+1)*(4+1)
# 아예 안입엇을 경우가 +1 => ans-1

T = int(input())

for t in range(T):
    N = int(input())
    total = {}
    result = 1
    for n in range(N):
        name, category = input().split()
        if category in total:
            total[category] += 1
        else:
            total[category] = 0
            total[category] += 1
    for value in total.values():
        result *= (value+1)
    print(result-1)