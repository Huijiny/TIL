def solution(genres, plays):
    answer = []
    my_album = {}
    for i in range(len(genres)):
        my_album[genres[i]] = my_album.get(genres[i], [])
        inner_album = my_album.get(genres[i])
        inner_album.append((i, plays[i]))
    total = {}
    for key, values in my_album.items():
        for value in values:
            total[key] = total.get(key, 0) + value[1]

    for key, values in my_album.items():
        my_album[key] = sorted(values, key=lambda x:x[1], reverse=True)
    total = sorted(total.items(), key=lambda  x:x[1], reverse=True)

    for genre in total:
        gen = genre[0]
        tmp = my_album.get(gen)
        if len(tmp) > 2:
            tmp = tmp[:2]
        while tmp:
            t = tmp.pop(0)
            answer.append(t[0])

    return answer


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
