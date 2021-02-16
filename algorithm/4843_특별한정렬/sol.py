import sys

sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr = [0]*N
    result = []

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for i in range(5):
        result.append(str(arr[N-i-1]))
        result.append(str(arr[i]))


    print("#{} {}".format(tc, ' '.join(result)))