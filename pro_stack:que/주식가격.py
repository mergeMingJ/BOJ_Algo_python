from collections import deque
def solution(price):
    answer = []
    prices = deque(price)
    while prices:
        flag = 0
        cnt = 0
        cost = prices.popleft()
        for money in prices:
            if cost <= money:
                cnt += 1
            else:
                flag = 1
                break
        if flag == 1:
            cnt += 1
        answer.append(cnt)

    return answer

print(solution([1, 2, 3, 2, 3]))

print('q', solution([1, 2, 3, 2, 3, 3, 1]))
