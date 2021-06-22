import sys
sys.stdin = open('input/17608.txt', 'r')

# 시간 초과나면 sys.stdin.readline을 input 대신 쓰기
# import sys
# input = sys.stdin.readline

T = int(input())
floor = []
showing = []
temp = -1

for t in range(T):
    # floor.appen(int(sys.stdin.readline())
    floor.append(int(input()))

for i in range(len(floor)-1, -1,-1):
    if temp >= floor[i]:
        pass
    else:
        temp = floor[i]

        if len(showing) == 0:
            showing.append(temp)
        else:
            last = showing[len(showing)-1]
            if last > temp:
                pass
            else:
                showing.append(temp)
print(len(showing))