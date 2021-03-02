import sys
sys.stdin = open("input (4).txt")

def recursive(n, m):
    if m == 1:
        return n
    else:
        return n * recursive(n, m-1)

T = 10
for tc in range(1, T+1):
    input()
    n, m = list(map(int, input().split()))
    result = recursive(n, m)


    print("#{} {}".format(tc, result))