import sys
sys.stdin = open("input (4).txt")

T = int(input())

for tc in range(1, 1+T):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    sizes = []
    # 행 우선순회 방식으로 순회하면서 사각형의 시작 좌표를 구한다.
    for col in range(n):
        for row in range(n):
            if matrix[col][row] != 0:
                lt = (col, row)
                dc, dr = col, row

                while dc < n and matrix[dc][row] != 0:
                    dc += 1
                while dr < n and matrix[col][dr] != 0:
                    dr += 1

                sizes.append((dc-col, dr-row))
                for i in range(col, dc):
                    for j in range(row, dr):
                        matrix[i][j] = 0


    sizes.sort(key=lambda x: (x[0] * x[1], x[0]))
    print("#{} {}".format(tc, len(sizes)), end=' ')
    for size in sizes:
        print("{} {}".format(size[0], size[1]), end=' ')
    print()