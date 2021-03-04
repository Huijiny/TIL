import sys
sys.stdin = open("input (4).txt")

T = 10
for tc in range(1, T+1):
    case = input()
    queue = list(map(int, input().split()))

    gap = 0
    while True:
        gap += 1
        first = queue.pop(0)
        next_ = first - gap
        if next_ <= 0:
            queue.append(0)
            break
        else:
            queue.append(next_)
        if gap == 5:
            gap = 0

    print("#{} {}".format(tc, ' '.join(list(map(str,queue)))))

