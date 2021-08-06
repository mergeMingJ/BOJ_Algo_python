# value 기준으로 정렬할때!
# music_dict = sorted(music_dict.items(), key=lambda x: x[1], reverse=True)


def solution(genres, plays):
    answer = []
    music = [[0, 0, 0] for _ in range(len(plays))]
    music_dict = {}

    for k in range(len(genres)):
        music[k][0] = genres[k]
        music[k][1] = plays[k]
        music[k][2] = k

        if genres[k] not in music_dict:
            music_dict[genres[k]] = plays[k]
        else:
            music_dict[genres[k]] += plays[k]
    music_dict = sorted(music_dict.items(), key=lambda x:x[1], reverse=True)

    for musics in music_dict:
        checks = []
        for i in range(len(music)):
            if musics[0] == music[i][0]:
                checks.append([music[i][1], music[i][2]])
        if checks:
            checks = sorted(checks, reverse=True)
            for c in range(len(checks)-1):
                if checks[c][0] == checks[c+1][0]:
                    if checks[c][1] > checks[c+1][1]:
                        item = checks.pop(c+1)
                        checks.insert(c, item)
            for check in checks[:2]:
                answer.append(check[1])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2500]))