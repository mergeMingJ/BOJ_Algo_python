import sys
sys.stdin = open('input/14501.txt', 'r')

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
arr.insert(0, [0,0])

total = [0] * (N+1)

# N만큼 돌면서 검사
for i in range(1, N+1):
    # 만약 현재 날짜와 끝나는 날짜를 했을때 기간내에 끝낼 수 있다면
    if i + arr[i][0] <= N+1:
        # 현재 날짜까 벌수 있는 돈 기록
        total[i] = arr[i][1]
        # 현재까지 날짜를 되돌아 보면서 추가
        for j in range(i):
            # 현재 날짜 내에 수행할 수 있다면
            if j + arr[j][0] <= i:
                # 기존의 수행값과 새로운 값중 가장 큰 값을 기록
                total[i] = max(total[i], total[j] + arr[i][1])
                # 총 토탈리스트 중에서 가장 큰 돈을 벌수 있는 값 출력
print(max(total))



