import sys
sys.stdin = open("sample_input (1).txt")
def dp(N):
    arr = [1, 3]
    if N == 1:
        return arr[0]
    elif N == 2:
        return arr[1]
    else:
        for i in range(2, N):
            arr.append(arr[i-1] + arr[i-2]*2)
    return arr[N-1]
T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10
    print("#{} {}".format(tc, dp(N)))