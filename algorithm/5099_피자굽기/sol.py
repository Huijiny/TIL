import sys
sys.stdin = open("sample_input (1).txt")

T = int(input())

for tc in range(1, T+1):
    size, pizza_count = map(int, input().split())
    chesse_amount = list(map(int, input().split()))
    pizza_check = [i for i in range(len(chesse_amount))]
    hwaduk = pizza_check[0:size]
    current = size - 1
    while len(hwaduk) != 1:
        pizza_idx = hwaduk.pop(0)# 하나를 일단 뽑아
        chesse_amount[pizza_idx] = chesse_amount[pizza_idx] // 2 # 치즈량을 계산하고
        if chesse_amount[pizza_idx] <= 0 : # 치즈량이 0 이하면 빼고 다음걸 넣고
            current += 1
            if current < len(chesse_amount):
                hwaduk.append(pizza_check[current])
        else: # 아니면 그대로 append
            hwaduk.append(pizza_idx)

    print("#{} {}".format(tc, hwaduk.pop(0) + 1))