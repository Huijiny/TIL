import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    move = [0] * 201
    for _ in range(N):
        a, b = map(int, input().split())
        if a > b: a, b = b, a
        a = (a+1)//2
        b = (b+1)//2
        for i in range(a, b+1):
            move[i] += 1
    max_ = move[0]
    for i in range(1, len(move)):
        if max_ < move[i]:
            max_ = move[i]
    print("#{} {}".format(tc, max_))