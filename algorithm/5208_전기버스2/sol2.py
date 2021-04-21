def bus_check(current):
    global cnt, charge
    # 다음 범위는 0 + 첫번재 배터리가 갈 수 있는 양
    next_range = current + charges[0]
    # 만약에 현재 위치가 전체길이 -1 일 경우까지만 와일문 돌아.
    while current < N-1:
        # 다음 범위가 N-1이거나 넘었으면 리턴해줌
        if next_range >= N-1:
            return
        # 다음 인덱스 초기화
        next_idx = 0
        # 최대 용량 초기화
        max_charge = 0
        # 현재 위치부터 다음 범위까지
        for i in range(current+1, next_range+1):
            # 현재 차지가 최대용량보다 크거나 같으면 최대용량을 바꿔주고 다음 인덱스 바꿔줘
            if charges[i] >= max_charge:
                max_charge = charges[i]
                next_idx = i

        cnt += 1
        charge -= next_idx - current
        charge += max_charge
        current = next_idx
        next_range = current + charge
    return

T = int(input())
for tc in range(1, T+1):
    min_count = 99999
    values = list(map(int, input().split()))
    N = values[0]
    charges = values[1:] + [0]
    last = len(charges) - 1
    bus_check(0, 0)
    print("#{} {}".format(tc, min_count))