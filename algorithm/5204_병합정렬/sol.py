import sys
sys.stdin = open('sample_input (3).txt')

def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2

    left = lst[:mid]
    right = lst[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    l = r = 0
    sorted_lst = []
    while l < len(sorted_left) and r < len(sorted_right):
        if sorted_left[l] < sorted_right[r]:
            sorted_lst.append(sorted_left[l])
            l += 1
        else:
            sorted_lst.append(sorted_right[r])
            r += 1

    sorted_lst += sorted_right[r:]
    sorted_lst += sorted_left[l:]

    return sorted_lst

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))
    print("#{} {}".format(tc, merge_sort(nums)))
