import sys

sys.stdin = open("2번_input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 첫번째로 주사위를 굴리는 사람 체크
    first_turn = input()
    # A, B 각각의 주사위 수 입력받기
    A_dice = list(map(int,input().split()))
    B_dice = list(map(int,input().split()))
    # A, B 각각의 위치 초기화
    A = B = 1
    # 주사위 배열을 돌 idx 초기화
    dice_idx = 0
    result = ''

    # A, B가 각각 20 일때까지 돌게 되는데,
    while A < 20 and B < 20:
        # 주사위를 10번 모두 돌리게 되면 결과는 무승부.
        if dice_idx == 10:
            result = 'AB'
            break
        # A가 먼저 시작했다면, A 부터 말을 옮기기 시작.
        if first_turn == 'A':
            A += A_dice[dice_idx] # 주사위만큼 말 옮기기
            if A >= 20: # 20넘었으면 승자 A
                result = 'A'
                break
            elif A == B: # 또는 B를 잡았다면 B 처음으로 돌리기
                B = 1

            B += B_dice[dice_idx] # 주사위만큼 말 옮기기
            if B >= 20: # 20 넘었으면 승자 B
                result = 'B'
                break
            elif A == B: # A를 잡았다면 A 처음으로 돌리기
                A = 1
            dice_idx += 1 # A와 B가 각각 주사위 한 턴을 돌았으므로 다음 주사위 돌리기

        # B가 먼저 시작했다면, B 부터 말을 옮기기 시작
        elif first_turn == 'B':
            B += B_dice[dice_idx] # 말 옮기기
            if B >= 20: # 승자 체크
                result = 'B'
                break
            elif A == B: # 말 잡았는지 체크
                A = 1

            A += A_dice[dice_idx] # 말 옮기기
            if A >= 20: # 승자체크
                result = 'A'
                break
            elif A == B: # 말잡았는지 체크
                B = 1
            dice_idx += 1 # 한 턴 돌아서 다음 주사위 돌리기

    print("#{} {}".format(tc, result))
