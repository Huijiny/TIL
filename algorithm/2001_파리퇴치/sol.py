import sys

sys.stdin = open("input (2).txt")

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    max = 0

    count = (N-M+1)
    for j in range(count):
        for i in range(count):
            total = 0
            for col in range(j, j+M):
                for row in range(i, i+M):
                    total += matrix[col][row]
            if max < total:
                max = total


    print("#{} {}".format(tc, max))