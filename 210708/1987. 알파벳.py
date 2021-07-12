import sys
sys.stdin = open('input/1987.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def DFS(x, y, cnt):
    global count

    count = max(count, cnt)

    for k in range(4):
        tx, ty = x+dx[k], y+dy[k]

        if tx < 0 or tx >= R or ty < 0 or ty >= C or arr[tx][ty] in check:
            continue
        else:
            check.append(arr[tx][ty])
            DFS(tx, ty, cnt+1)
            check.remove(arr[tx][ty])




R, C = map(int,input().split())
arr = [[str(a) for a in ('').join(input().split())] for _ in range(R)]
total = []
global count
check = []
count = 1
check.append(arr[0][0])
DFS(0, 0, count)
print(count)
# 시간초과!!
# 다시 풀어보자 내일!
