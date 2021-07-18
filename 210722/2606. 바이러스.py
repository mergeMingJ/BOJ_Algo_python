import sys
sys.stdin = open('input/2606.txt')


def check_relation(num):
    global cnt

    if check[num] == 0:
        check[num] = 1
        cnt += 1

        for n in relation[num]:
            check_relation(n)


N = int(input())
P = int(input())
connect = [[int(a) for a in input().split()] for _ in range(P)]
relation = []
check = [0] * (N+1)
global cnt
cnt = -1

for k in range(N+1):
    relation.append([])

for item in connect:
    relation[item[0]].append(item[1])
    relation[item[1]].append(item[0])

check_relation(1)
print(cnt)


