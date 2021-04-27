import sys
sys.stdin = open('sample_input (3).txt')


# def partition(numbers, left, right):
#     pivot = numbers[left]
#     start = left + 1
#     end = right
#
#     while start <= end:
#         while start <= end and numbers[start] <= pivot:
#             start += 1
#         while start <= end and numbers[end] >= pivot:
#             end -= 1
#         numbers[start], numbers[end] = numbers[end], numbers[start]
#     numbers[left], numbers[end] = numbers[end], numbers[start]
#     return end
#
# def quick_sort(numbers, left, right):
#     if left < right:
#         pivot = partition(numbers, left, right)
#         quick_sort(numbers, left, pivot - 1)
#         quick_sort(numbers, pivot + 1, right)


def partition(numbers, start, end):
    pivot = numbers[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= right and numbers[left] <= pivot:
            left += 1
        while left <= right and numbers[right] >= pivot:
            right -= 1
        numbers[left], numbers[right] = numbers[right], numbers[left]
    numbers[start], numbers[right] = numbers[right], numbers[start]
    return right


def quick_sort(numbers, start, end):
    if start < end:
        pivot = partition(numbers, start, end)
        quick_sort(numbers, start, pivot - 1)
        quick_sort(numbers, pivot + 1, end)

for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, N-1)
    print(numbers)
    print("#{} {}".format(tc, numbers[N//2]))