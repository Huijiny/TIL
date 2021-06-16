import sys
sys.stdin = open('sample')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    weights = list(map(int, input().split()))
    max_value = 0
    def solution(arr, val):
        global max_value
        if len(arr) == 2:
            if max_value < val:
                max_value = val
        else:
            for i in range(1, len(arr)-1):
                tmparr = arr[:i] + arr[i+1:]
                solution(tmparr, val + arr[i-1] * arr[i+1])
    solution(weights, 0)
    print(max_value)