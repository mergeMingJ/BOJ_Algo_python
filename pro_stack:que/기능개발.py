import math

def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        todo = 100 - progresses[i]
        days.append(math.ceil(todo / speeds[i]))
    print(days)
    while days:
        start = days.pop(0)
        if start == -1:
            continue
        cnt = 1
        k = 0
        for j in range(k, len(days)):
            if start >= days[j]:
                cnt += 1
                days[j] = -1
            else:
                break
        answer.append(cnt)
        if k == len(days):
            break

    return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))