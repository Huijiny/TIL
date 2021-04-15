import sys
sys.stdin = open("sample_input (3).txt")

def search(col, row, sum_):
    global min_sum
    if col < N and row < N:
        sum_ += matrix[col][row]
        if sum_ > min_sum:
            return
        if col == N-1 and row == N-1:
            if sum_ < min_sum:
                min_sum = sum_
            return
        else:
            search(col+1, row, sum_)
            search(col, row+1, sum_)

T = int(input())

for tc in range(1, T+1):
    sum_ = 0
    min_sum = 9999999
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    search(0, 0, 0)
    print("#{} {}".format(tc, min_sum))