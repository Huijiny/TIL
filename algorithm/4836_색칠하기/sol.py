import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

for tc in range(1, T+1):
    matrix_n = 10
    result = 0
    m_row = [0] * matrix_n
    matrix = []
    for _ in range(matrix_n):
        matrix.append(list(m_row))

    N = int(input())

    for _ in range(N):
        points = list(map(int, input().split()))
        for col in range(points[1], points[3]+1):
            for row in range(points[0], points[2]+1):
                if matrix[col][row] != 0 and matrix[col][row] != points[4]:
                    result += 1
                matrix[col][row] = points[4]


    print("#{} {}".format(tc, result))