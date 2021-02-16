import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    m_row = [0] * N
    matrix = []
    for _ in range(N):
        matrix.append(list(m_row))
    matrix[0][0] = 1
    round = 1
    row, col = 0
    left, up, down = 0
    right = 1
    for i in range(2, (N*N)+1):
        if right and row <= N-round:
            row += 1
            if row == N-round:
                right = 0
                down = 1
        elif down and col <= N-round:
            col += 1
            if col == N-round:
                down = 0
                left = 1
        elif left and row >= round-1:
            row -= 1
            if row == round-1:
                left = 0
                up = 1
                round += 1
        elif up and col >= round-1:
            col -= 1
            matrix[col][row] = i
            if col == round-1:
                up = 0
                right = 1
        matrix[col][row] = i

    print("#{}".format(tc))
    for col in range(N):
        for row in range(N):
            print(matrix[col][row], end=' ')
        print()