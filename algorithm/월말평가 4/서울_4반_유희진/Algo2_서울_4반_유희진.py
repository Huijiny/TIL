def binary_search(target, M):
    left = 0
    right = M - 1
    cnt = 0
    # 왼쪽이 항상 오른쪽보다 작거나 같고
    while left <= right:
        # 가운데 깂
        mid = (left + right) // 2
        # 타겟값이면 리턴
        if numbers[mid] == target:
            return cnt + 1
        # 타겟이 중점보다 크면 오른쪽 라벨을 옮김
        elif numbers[mid] < target:
            left = mid + 1
        # 타겟이 중점보다 작으면 왼쪽 라벨을 옮
        else:
            right = mid - 1
        cnt += 1
    return None
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    targets = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    # 타겟 결과를 모두 모을 리스트
    target_result = []
    min_result = 0
    # 타겟 값들을 돌면서
    for target in targets:
        # 이진탐색해서 찾아온 횟수
        count = binary_search(target, N)
        # 못찾았으면 다음 타겟
        if count == None:
            continue
        # 아니면 타겟 리절트에 추가해
        else:
            target_result.append((target, count))
    # 타겟 결과를 카운트 값으로 소팅함
    target_result.sort(key=lambda x:x[1])
    # 첫번째 값이 젤 카운트 작은 값
    min_result = target_result[0][1]
    options = []
    # 카운트 작은 값이 여러개 있나 체크
    for target in target_result:
        if target[1] == min_result:
            options.append(target)
    # 여러개면 타겟값으로 소팅함.
    if len(target) > 1:
        options.sort(key=lambda x:x[0])


    print("#{} {} {}".format(tc, options[0][0], options[0][1]))