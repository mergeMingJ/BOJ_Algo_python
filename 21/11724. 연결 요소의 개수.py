import sys
sys.stdin = open('input/11724.txt', 'r')


def bfs(s):
    visit = [False] * (V + 1)
    D = [0] * (V + 1)
    Q = []
    Q.append(s)
    visit[s] = True
    #print(s, end=" ")

    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visit[w]:
                D[w] = D[v] + 1
                visit[w] = True
                Q.append(w)
    return D


V,E = list(map(int, input().split()))
G = [[] for _ in range(V + 1)]

for e in range(E):
    start, end = map(int, input().split())
    G[start].append(end)
    G[end].append(start)
print(G)

for i in range(1,V+1):
    D = bfs(i)

    print(D)



