import sys
sys.stdin = open("sample_input (2).txt")

def find(n):
    global result
    if n >= 1:
        result += tree[n]
        find(n//2)


def sort(i):
    if i > 1:
        if tree[i] < tree[i//2]:
            tree[i], tree[i//2] = tree[i//2], tree[i]
            sort(i//2)


T = int(input())
for tc in range(1, T+1):
    result = 0
    N = int(input())
    tree = [0] * (N+1)
    values = list(map(int, input().split()))
    for i in range(1, N+1):
        tree[i] = values[i-1]
        sort(i)
    find(N//2)
    print("#{} {}".format(tc, result))