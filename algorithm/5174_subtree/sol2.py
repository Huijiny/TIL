import sys
sys.stdin = open("sample_input (2).txt")


def inorder(N):
    global result
    # N이 0 이상인 경우에만 순회
    if N > 0:
        result += 1
        inorder(tree[0][N])
        inorder(tree[1][N])

T = int(input())

for tc in range(1, T+1):
    result = 0
    E, N = map(int, input().split())
    tree = [[0] * (E+2) for _ in range(2)]

    values = list(map(int, input().split()))
    #
    for i in range(E):
        pa, ch = values[i*2], values[i*2+1]
        if tree[0][pa] == 0:
            tree[0][pa] = ch
        else:
            tree[1][pa] = ch
    inorder(N)
    print(tree)

    print("{} {}".format(tc, result))