def solution(places):
    answer = []
    for place in places:
        room = []
        for people in place:
            room.append(list(people))
        isOk = True
        di = [1, -1, 0, 0]
        dj = [0, 0, 1, -1]

        oi = [1, -1, 1, -1]
        oj = [1, -1, -1, 1]
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':

                    # 4방에 두칸씩 확인
                    for z in range(4):
                        # 한 방향을 두 번씩 확인
                        for _ in range(2):
                            ni, nj = i + di[z], j + dj[z]
                            # 만약에 범위 안에면,
                            if 0 <= ni < 5 and 0 <= nj < 5:
                                # 한칸 갔는데 사람있으면 break.
                                if room[ni][nj] == 'P':
                                    isOk = False
                                    break
                                # 더이상 그 방향으로 갈 필요 없음.
                                if room[ni][nj] == 'X':
                                    break

                    # 4방향 돌아도 괜찮았으면 대각선 확인.
                    if isOk:
                        for z in range(4):
                            ni, nj = i + oi[z], j + oj[z]
                            # 대각선 범위 안, + 그 자리가 사람이면,
                            if 0 <= ni < 5 and 0 <= nj < 5 and room[ni][nj] == 'P':
                                # 대각선 방향 둘 다 파티션이면
                                if room[i][nj] == 'X' and room[ni][j] == 'X':
                                    isOk = True
                                # 그게 아니면,
                                else:
                                    isOk = False

                if not isOk:
                    break
            if not isOk:
                break
        answer.append(int(isOk))
    print(answer)
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])