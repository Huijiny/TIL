def is_babygin(baby):
    answer = 0
    # 만약에 카운팅이 3 이상이면 체크하고 1 올려줘
    for t in range(len(baby)):
        if baby[t] >= 3:
            baby[t] -= 3
            answer += 1
    # 연속된 3 자리를 계속 체크하면서 모두 다 있으면 1올리고 그 자리 하나씩 빼줘
    for i in range(8):
        if baby[i] and baby[i+1] and baby[i+2]:
            baby[i] -= 1
            baby[i+1] -= 1
            baby[i+2] -= 2
            answer += 1
    # answer 가 2라는게 트리팔렛이나 런 둘 중 두개 있다는 것.
    # 두개면 True, 아니면 False
    if answer == 2:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input()))
    counting = [0] * 10
    for num in numbers:
        counting[num] += 1

    if is_babygin(counting):
        result = 1
    else:
        result = 0
    print("#{} {}".format(tc, result))