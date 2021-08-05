from collections import deque


def solution(prior, location):
    answer = 0
    prior = deque(prior)
    result = []
    order = [[0, 0] for _ in range(len(prior))]
    max_value = max(prior)

    for i in range(len(prior)):
        order[i][0] = i
        order[i][1] = prior[i]

    while order:
        index, value = order.pop(0)
        if len(order) == 0:
            result.append([index, value])
        else:
            if max_value == value:
                result.append([index, value])
                prior.remove(value)
                max_value = max(prior)
            else:
                order.append([index, value])

    for k in range(len(result)):
        if result[k][0] == location:
            answer = k+1

    return answer

print(5, solution([1, 1, 9, 1, 1, 1], 0))
print(1, solution([2, 1, 3, 2], 2))
