import sys
sys.stdin = open('input/2178.txt', 'r')
import collections

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [[int(a) for a in ('').join(input().split())] for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
Q = collections.deque()

Q.append([0,0])
visit[0][0] = 1

while Q:
    x, y = Q.popleft()

    for t in range(4):
        tx, ty = x + dx[t], y + dy[t]

        if tx < 0 or tx >= M or ty < 0 or ty >= N or visit[ty][tx] != 0 or arr[ty][tx] == 0:
            continue
        else:
            Q.append([tx, ty])
            visit[ty][tx] = visit[y][x] + 1
print(visit[N-1][M-1])

