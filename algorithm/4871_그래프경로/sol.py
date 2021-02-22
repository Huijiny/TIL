import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    matrix = [[0]*V for _ in range(V)]
    for _ in range(E):
        f, t = list(map(int, input().split()))
        matrix[f-1][t-1] = 1
    S, G = list(map(int, input().split()))
    # 여기서 이제 어디갔다가 어디갔다가 어디가는지 찾아야함.
    stack = []


    print("#{} {}".format(tc))