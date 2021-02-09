import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        max = boxes[0]
        max_idx = 0
        min = boxes[0]
        min_idx = 0

        for i in range(1, len(boxes)):
            if max < boxes[i]:
                max = boxes[i]
                max_idx = i
            if min > boxes[i]:
                min = boxes[i]
                min_idx = i

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    max = boxes[0]
    min = boxes[0]
    for i in range(1, len(boxes)):
        if max < boxes[i]:
            max = boxes[i]
        if min > boxes[i]:
            min = boxes[i]
    print('#{} {}'.format(tc, max-min))