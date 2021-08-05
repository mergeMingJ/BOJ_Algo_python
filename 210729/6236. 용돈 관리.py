import sys
sys.stdin = open('input/6236.txt', 'r')

N, M = map(int, input().split())
costs = []
for _ in range(N):
    costs.append(int(input()))

answer, left, right = sum(costs), 0, sum(costs)

while left <= right:
    mid_value = (left + right) // 2
    count, money = 0, 0
    lack = False

    for cost in costs:
        if mid_value - cost < 0:
            # 돈을 뽑아도 하루를 못 넘기면
            lack = True
            break
        elif money - cost < 0:
            money = mid_value
            count += 1
        money -= cost

    # 돈이 부족한 날이 없으면
    if not lack:
        # 목표 횟수보다 count가 같거나 작으면 돈을 줄임
        if count <= M:
            right = mid_value - 1
            if mid_value < answer:
                answer = mid_value
        # 목표 횟수보다 count가 크면 돈을 늘림
        elif count > M:
            left = mid_value + 1
    # 돈이 부족한 날이 있으면 무조건 돈을 늘림
    else:
        left = mid_value + 1

print(answer)

