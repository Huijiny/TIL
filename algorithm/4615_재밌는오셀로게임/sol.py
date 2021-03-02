import sys
sys.stdin = open("sample_input(1).txt")
# global 키워드 => 함수 바깥의 변수를 "재할당" 할 때. 아예 판을 다시 짤 때. 이미있던거 바꾸는거 말고.

def checker(row, col, color):
    matrix[col][row] = color

    # 9방향 델타이동.
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            # 단, 지금 돌을 둔 위치는 볼 필요가 없다.
            if dx == dy == 0:
                continue
            # 현재 탐색 방향 일직선 안에서 지금 둔 돌과 색이 같고
            # 동시에 사이에 다른 돌이 낀 돌의 좌표(cx, cy)
            ccol = col + dy
            crow = row + dx
            found = False # 진행하다가 지금 color와 같은 애를 찾아야해.

            # 게임판 범위 내에서
            while 0 <= crow < N and 0 <= ccol < N:
                # 내 돌과 다른색 돌이 나온다면 계속 전진
                if matrix[ccol][crow] == 3 - color:
                    ccol += dy
                    crow += dx
                # 하다가, 같은색이 나왔다면 STOP!
                elif matrix[ccol][crow] == color:
                    found = True
                    break
                #빈칸이 나오면 그냥 정지!
                else:
                    break
            if found:
                # px, py는 이동할 때 쓸 idx
                # x ~ px >>>> ~ cx / y ~ py ~ cy
                px, py = row+dx, col+dy
                while px != crow or py != ccol:
                    matrix[py][px] = color
                    px += dx
                    py += dy
T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [[0] * N for _ in range(N)]
    mid_idx = N // 2 - 1
    matrix[mid_idx][mid_idx] = matrix[mid_idx+1][mid_idx+1] = 2
    matrix[mid_idx][mid_idx+1] = matrix[mid_idx+1][mid_idx] = 1

    for _ in range(M):
        row, col, color = list(map(int,input().split()))
        checker(row-1, col-1, color)

    black = white = 0
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 1:
                black += 1
            elif matrix[y][x] == 2:
                white += 1


    print("#{} {} {}".format(tc, black, white))