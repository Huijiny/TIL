import sys
sys.stdin = open("input (4).txt")

def search(count):
    global max_val
    value = int(''.join(numbers))
    if value in visited[count]:
        return
    visited[count].add(value)

    if count == 0:
        visited[count].add(value)
        max_val = max(max_val, value)
        return
    else:
        for i in range(N - 1):
            for j in range(i + 1, N):
                # 스왑
                numbers[i], numbers[j] = numbers[j], numbers[i]
                search(count - 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]

T = int(input())
for tc in range(1, T+1):
    max_val = 0
    numbers, count = input().split()
    numbers = list(numbers)
    N = len(numbers)
    count = int(count)
    visited = [set() for _ in range(11)]
    search(count)
    print("#{} {}".format(tc,max_val))


