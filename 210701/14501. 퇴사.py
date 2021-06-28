import sys
sys.stdin = open('input/14501.txt', 'r')

N = int(input())


arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0,0])
result = []
for i in range(1, N+1):
    work = i
    hap = 0

    while True:
        days, price = arr[work][0]-1, arr[work][1]
        if work+days > N:
            result.append(hap)
            break
        elif work+days == N:
            hap += price
            result.append(hap)
            break
        else:
            hap += price
            work = work+days+1
    print(result)
print(max(result))
# 푸는중... 

