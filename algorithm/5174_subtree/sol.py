def preorder(n):
    global count
    if n > 0:
        count += 1
        preorder(chs[0][n])
        preorder(chs[1][n])

import sys
sys.stdin = open("sample_input (2).txt")
T = int(input())
for tc in range(1, T+1):
    count = 0
    result = 0
    E, N = map(int, input().split())
    values = list(map(int, input().split()))
    chs = [[0] * (E + 2) for _ in range(2)]
    for i in range(E):
        n1, n2 = values[i*2], values[i*2+1]
        if chs[0][n1] == 0:
            chs[0][n1] = n2
        else:
            chs[1][n1] = n2
    preorder(N)
    print(("#{} {}".format(tc, count)))