import sys
sys.stdin = open("sample_input (3).txt")


def partition(data, start, end):
    x = data[end]
    i = start - 1
    for j in range(start, end):
        if data[j] <= x:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[end] = data[end], data[i + 1]
    return i + 1

def partition2(arr, l, r):
    pass

def lomuto(arr, l, r):
    # 종료 조건
    if l >= r:
        return
    # 피봇설정 맨 앞에 것.
    x = arr[r]
    i = l - 1
    j = l
    while j < r:
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    pivot = i + 1

    # 새로운 피봇 = right를 기준으로 왼쪽과 오른쪽을 나눠 소트
    lomuto(arr, l, pivot - 1)
    lomuto(arr, pivot + 1, r)


for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    lomuto(numbers, 0, N-1)
    print("#{} {}".format(tc, numbers[N//2]))