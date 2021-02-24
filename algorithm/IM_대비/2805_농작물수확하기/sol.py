import sys
sys.stdin = open("input (4).txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    mid = N//2 + 1
    total = 0
    idx = mid
    for col in range(N):
        if col < mid-1:
            for row in range(mid-col-1, mid+col):
                total += matrix[col][row]
        elif col == mid-1:
            for row in range(N):
                total += matrix[col][row]
        elif col > mid-1:
            for row in range(mid-col-1+(2*(col-(mid-1))), mid+col-(2*(col-(mid-1)))):
                total += matrix[col][row]

    print("#{} {}".format(tc, total))