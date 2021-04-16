import sys
sys.stdin = open("sample_input (3).txt")

def is_babygin(baby):
    if len(baby) >= 3:
        for t in baby:
            if t >= 3:
                return True
        for i in range(8):
            if baby[i] > 0 and baby[i+1] > 0 and baby[i+2] > 0:
                return True
    return False


T = int(input())
for tc in range(1, T+1):
    result = 0
    values = list(map(int, input().split()))
    # 각 플레이어 카드 카운팅 할 배열
    baby1 = [0] * 10
    baby2 = [0] * 10
    b1 = b2 = False

    for i in range(6):
        # 첫 번째 플레이어.
        baby1[values[i*2]] += 1
        if is_babygin(baby1):
            b1 = True
        # 두 번째 플레이어.
        baby2[values[i*2+1]] += 1
        if is_babygin(baby2):
            b2 = True

        # b1, b2 가 둘 다 True면 무승부
        if b1 and b2:
            result = 0
            break
        # 둘 중 하나만 True면 True인 사람 승자 및 break
        if b1 or b2:
            result = 1 if b1 else 2
            break
    # 둘 다 False면 무승
    print("#{} {}".format(tc, result))