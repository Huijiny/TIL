import sys
sys.stdin = open("sample_input (3).txt")

def is_babygin(baby):
    for t in baby:
        if t >= 3:
            return True
    for i in range(8):
        if baby[i] and baby[i+1] and baby[i+2]:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    result = 0
    cards = list(map(int, input().split()))
    # 각 플레이어 카드 카운팅 할 배열
    baby1 = [0] * 10
    baby2 = [0] * 10

    for i in range(6):
        # 첫 번째 플레이어.
        baby1[cards[i*2]] += 1
        if i >= 2 and is_babygin(baby1):
            result = 1
            break
        # 두 번째 플레이어.
        baby2[cards[i*2+1]] += 1
        if i >= 2 and is_babygin(baby2):
            result = 2
            break

    print("#{} {}".format(tc, result))