import sys
sys.stdin = open("input (3).txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    m1 = [[] for _ in range(N)]

    for row in range(N):
        tmp = ''
        for col in range(N-1, -1, -1):
            tmp += str(matrix[col][row])
        m1[row].append(tmp)

    for col in range(N-1, -1, -1):
        tmp = ''
        for row in range(N-1, -1, -1):
            tmp += str(matrix[col][row])
        m1[N-1-col].append(tmp)

    for row in range(N-1, -1, -1):
        tmp = ''
        for col in range(N):
            tmp += str(matrix[col][row])
        m1[N-1-row].append(tmp)

    print("#{}".format(tc))
    for i in range(N):
        print(*m1[i])