import sys
sys.stdin = open("input (4).txt")


def inorder(n):
    if n <= N:
        inorder(n*2)
        print(tree[n], end='')
        inorder(n*2 + 1)
T = 10

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)

    for i in range(1, N+1):
        tree[i] = input().split()[1]

    print("#{}".format(tc), end=' ')
    inorder(1)
    print()