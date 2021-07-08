import sys
sys.stdin = open('input/14501.txt', 'r')

N = int(input())
arrs = [[int(k) for k in input().split()] for _ in range(N)]
arrs.insert(0, [0,0])
dp = [0] * (N+2)

for i in range(1, len(arrs)):
    day, cost = arrs[i][0], arrs[i][1]

    # 이전값과 현재값 비교해서 이전값이 크다면 현재값 = 이전값
    if dp[i-1] > dp[i]:
        dp[i] = dp[i-1]

    # 범위 넘어가면 continue
    if i+day > N+1:
        continue
    else:
        if dp[i+day] < dp[i]+cost:
            update = dp[i]+cost
            # 갱신된 값 넣어주기
            dp[i+day] = update

print(max(dp))







