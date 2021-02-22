import sys
sys.stdin = open("input (3).txt")
def rotation(mtrx):
    new_m = []
    for _ in range(N):
        new_m.append([''] * N)

    for col in range(N):
        for row in range(N):

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    m1 = []
    for _ in range(N):
        m1.append([''] * N)
    for i in range(3):
        matrix = rotation(matrix)
    print("#{}".format(tc))