import sys
sys.stdin = open("sample_input (3).txt")

def postorder(n):
    idx1 = n*2
    idx2 = n*2+1
    if idx1 <= N:
        postorder(idx1)
        if idx2 <= N:
            postorder(idx2)
        else:
            idx2 = 0
        chs[n] = chs[idx1] + chs[idx2]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    chs = [0] * (N+1)
    for i in range(M):
        n1, n2 = map(int, input().split())
        chs[n1] = n2
    postorder(1)
    print("#{} {}".format(tc, chs[L]))