def solution(prices):
    answer = []
    num = 0
    n = 1
    for i in range(num, len(prices)):
        if i == len(prices) - 1:
            answer.append(0)
            continue

        cnt = 1
        for j in range(n, len(prices)-1):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                break
        answer.append(cnt)
        n+=1
        num += 1
        continue

    return answer

print(solution([1, 2, 3, 2, 3]))

print('q', solution([1, 2, 3, 2, 3, 3, 1]))
