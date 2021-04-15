import sys
sys.stdin = open("input (4).txt")

def search(count):
    global max_val
    if count == 0:
        val = int(''.join(numbers))
        already[val] = True
        if val > max_val:
            max_val = val
        return

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            val = int(''.join(numbers))
            if not already[val]:
                search(count-1)
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for tc in range(1, T+1):
    max_val = 0
    numbers, count = input().split()
    numbers = list(numbers)
    already = [False] * 999999
    count = int(count)
    search(count)
    print("#{} {}".format(tc, max_val))


