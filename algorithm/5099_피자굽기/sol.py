import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

for tc in range(1, T+1):
    size, pizza_count = map(int, input().split())
    chesse_amount = list(map(int, input().split()))

    hwaduk = [0] * size
    hwaduk_check = [[] for _ in range(len(chesse_amount))]
    for i in range(len(chesse_amount)):
        hwaduk_check[i].append(chesse_amount[i])
    for j in range(size):
        hwaduk[j] = j
    i = 0
    current = size-1
    while len(hwaduk) != 1:
        print(hwaduk_check[hwaduk[i]][0])
        hwaduk_check[hwaduk[i]][0] = hwaduk_check[hwaduk[i]][0] // 2
        if hwaduk_check[hwaduk[i]][0] <= 0:
            hwaduk[i] = current + 1
            hwaduk_check[i] = [chesse_amount[hwaduk[i]]]
            if current != len(chesse_amount) -1:
                current += 1
            else:
                hwaduk_check.pop(0)
        i = (i + 1) % size
    print("#{} {}".format(tc, hwaduk[i]))