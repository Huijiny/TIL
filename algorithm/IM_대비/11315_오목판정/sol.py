import sys

sys.stdin = open("sample_input.txt")


def solution(N, board):
    count_rl = count_lr = 0
    for i in range(N):
        # 대각선.
        if board[i][i] == 'o':
            count_lr += 1
            if count_lr == 5:
                return "YES"
        else:
            count_lr = 0

        if board[i][N-i-1] == 'o':
            count_rl += 1
            if count_rl == 5:
                return "YES"
        else:
            count_rl = 0

        count_r = count_c = 0
        for j in range(N):
            # 가로
            if board[i][j] == 'o':
                count_r += 1
                if count_r >= 5:
                    return "YES"
            else:
                count_r = 0
            # 세로
            if board[j][i] == 'o':
                count_c += 1
                if count_c >= 5:
                    return "YES"
            else:
                count_c = 0
    return "NO"


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    print("#{} {}".format(tc, solution(N, board)))
