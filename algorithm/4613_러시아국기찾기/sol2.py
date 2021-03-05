import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [list(input()) for _ in range(N)]

    print("#{} {}".format(tc, ))
