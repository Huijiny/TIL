import sys
sys.stdin = open('sample_input (3).txt')


def is_exist_diagnal(cur_pos):
    for queen in queens:
        if abs(cur_pos[0] - queen[0]) == abs(cur_pos[1] - queen[1]):
            return True
    return False


def n_queens(row):
    global visited, count
    if row == N:
        count += 1
    else:
        for col in range(N):
            # 같은 열에 다른 퀸이 존재하는지 체크
            if not visited[col] and not is_exist_diagnal((col, row)):
                visited[col] = True
                queens.append((col, row))
                n_queens(row + 1)
                queens.pop()
                visited[col] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0
    visited = [False] * N
    queens = []
    n_queens(0)
    print("#{} {}".format(tc, count))