def solution(answers):
    answer = []
    n = len(answers)
    ans_cnt = {1: 0, 2: 0, 3: 0}
    person1 = []
    person2 = []
    person3 = []

    for i in range(1, n+1):
        # 1번 학생 답지
        if i%5 == 0:
            person1.append(5)
        else:
            person1.append(i % 5)
        # 2번 학생 답지
        if i%2 != 0:
            person2.append(2)
        else:
            if i%8 == 2:
                person2.append(1)
            elif i%8 == 4:
                person2.append(3)
            elif i%8 == 6:
                person2.append(4)
            elif i%8 == 0:
                person2.append(5)
        # 3번 학생 답지
        if i%10 == 1 or i%10 == 2:
            person3.append(3)
        elif i%10 == 3 or i%10 == 4:
            person3.append(1)
        elif i%10 == 5 or i%10 == 6:
            person3.append(2)
        elif i%10 == 7 or i%10 == 8:
            person3.append(4)
        elif i%10 == 9 or i%10 == 0:
            person3.append(5)
    for k in range(len(answers)):
        if answers[k] == person1[k]:
            ans_cnt[1] += 1
        if answers[k] == person2[k]:
            ans_cnt[2] += 1
        if answers[k] == person3[k]:
            ans_cnt[3] += 1

    max_value = max(ans_cnt.values())
    for key in ans_cnt:
        if ans_cnt[key] == max_value:
            answer.append(key)

    return sorted(answer)

print(solution([1, 3, 2, 4, 2]))