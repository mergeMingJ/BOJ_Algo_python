def solution(n, losts, reserves):
    people = n - len(losts)
    losts = sorted(losts)

    for l in range(len(losts)):
        if losts[l] in reserves:
            people += 1
            reserves.remove(losts[l])
            losts[l] = -100
            continue

    for item in losts:
        can1 = item - 1
        can2 = item + 1
        if can1 in reserves:
            people += 1
            reserves.remove(can1)
            continue
        elif can2 in reserves:
            people += 1
            reserves.remove(can2)
            continue

    return people

print(solution(5, [1, 2, 4, 5], [2, 3, 4]))