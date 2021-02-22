import sys

sys.stdin = open("sample_input.txt")


def solution(N, board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                if j + 4 < N and i + 4 < N and board[i+1][j+1] =='o' and board[i+2][j+2]=='o' and board[i+3][j+3] == 'o' and board[i+4][j+4] == 'o':
                    return "YES"
                if i + 4 < N and j - 4 >= 0  and board[i+1][j-1] == 'o' and board[i+2][j-2]=='o' and board[i+3][j-3] == 'o' and board[i+4][j-4] == 'o':
                    return "YES"
    for i in range(N):
        count_r = count_c = 0
        for j in range(N):
            # 가로
            if board[i][j] == 'o':
                count_r += 1
                if count_r == 5:
                    return "YES"
            else:
                count_r = 0
            # 세로
            if board[j][i] == 'o':
                count_c += 1
                if count_c == 5:
                    return "YES"
            else:
                count_c = 0
    return "NO"


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]
    print("#{} {}".format(tc, solution(N, board)))
