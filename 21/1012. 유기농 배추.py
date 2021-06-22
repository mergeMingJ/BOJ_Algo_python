import sys
sys.stdin = open('input/1012.txt', 'r')
sys.setrecursionlimit(50000)


T = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    visit[x][y] = 1
    for d in range(4):
        tx, ty = x+dx[d], y+dy[d]

        if tx < 0 or tx >= N or ty < 0 or ty >= M or visit[tx][ty] == 1 or arr[tx][ty] == 0:
            continue
        else:
            dfs(tx,ty)


for t in range(T):
    M, N, K = list(map(int, input().split()))
    arr = [[0]*M for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    cnt = 0

    for k in range(K):
        a,b = map(int, input().split())
        arr[b][a] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visit[i][j] == 0:
                cnt+=1
                dfs(i, j)

    print(cnt)



