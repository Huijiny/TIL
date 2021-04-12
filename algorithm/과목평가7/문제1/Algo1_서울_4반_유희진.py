dcol = [1, 1, -1, -1]
drow = [1, -1, 1, -1]

def find():
    global result
    while bombs:
        # 현재 폭탄의 위치와 양 체크
        cur_col, cur_row, cur_power = bombs.pop(0)
        # 현재 위치 폭탄 사망자 체크
        result += map_[cur_col][cur_row]
        map_[cur_col][cur_row] = 0

        # delta 값으로 대각선 범위로
        for i in range(4):
            # 정해진 방향만큼 power만큼 돌아
            new_col = cur_col
            new_row = cur_row
            for _ in range(cur_power):
                new_col = new_col + dcol[i]
                new_row = new_row + drow[i]

                # 지도 범위 내에 있으면
                if 0 <= new_row < N and 0 <= new_col < N:
                    # 폭탄으로 죽은 사람 명 수 세고, 0으로 초기화
                    result += map_[new_col][new_row]
                    map_[new_col][new_row] = 0


T = int(input())

for tc in range(1, T+1):
    result = 0
    N, M = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(N)]
    bombs = []
    for i in range(M):
        bombs.append(list(map(int, input().split())))
    find()
    print("#{} {}".format(tc, result))