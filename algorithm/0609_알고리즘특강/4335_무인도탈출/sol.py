import sys
sys.stdin = open('sample_sample_input.txt')


T = int(input())

for tc in range(1, 4):
    box_cnt = int(input())
    boxess = [list(map(int, input().split())) for _ in range(box_cnt)]
    bs = [0] * len(boxess)
    real_max = 0
    def recursive(idx, max_val, boxes):
        global real_max

        if idx == len(boxess):
            print(bs)
            print("max values!",max_val)
            return

        # 만약에 맨 처음거라면 그냥 boxes에 추가만 해.
        if len(boxes) == 0:
            bs[idx] = 1
            boxes.append(boxess[idx])
            # 만약에 얘가 맨 첫번째 박스면, 각각의 길이가 height가 되도록 해
            for i in range(3):
                max_val[0] = boxes[0][i]
                if max_val[0] > real_max:
                    real_max = max_val[0]
                recursive(idx+1, max_val, boxes)

            max_val[0] = 0
            # 방금추가한 애 빼기
            bs[idx] = 0
            boxes.pop(0)
            recursive(idx+1, max_val, boxes)
        # 맨처음게 아니라 두번째꺼 부터면, 이 전에 추가된 박스랑 비교해.
        else:
            # 포함
            bs[idx] = 1
            sum_max = sum(max_val)
            # 1-1 가로 세로 높이
            if boxes[-1][0] >= boxess[idx][0] and boxes[-1][1] >= boxess[idx][1]:
                if real_max < sum_max:
                    real_max = sum_max
                recursive(idx + 1, max_val.append(boxess[idx][2]), boxes.append(boxess[idx]))

            # 1-2 세로 가로 높이
            if boxes[-1][1] >= boxess[idx][0] and boxes[-1][0] >= boxess[idx][1]:
                if real_max < sum_max:
                    real_max = sum_max
                recursive(idx + 1, max_val.append(boxess[idx][2]))

            # 1-3 높이 세로 가로
            if boxes[-1][2] >= boxess[idx][0] and boxes[-1][1] >= boxess[idx][1]:
                if real_max < sum_max:
                    real_max = sum_max
                recursive(idx + 1, max_val.append(boxess[idx][0]), boxes.append(boxess[idx]))

            # 1-4 세로 높이 가로
            if boxes[-1][1] >= boxess[idx][0] and boxes[-1][2] >= boxess[idx][1]:
                if real_max < sum_max:
                    real_max = sum_max
                recursive(idx + 1, max_val.append(boxess[idx][0]), boxes.append(boxess[idx]))

            # 1-5 가로 높이 세로
            if boxes[-1][0] >= boxess[idx][0] and boxes[-1][2] >= boxess[idx][1]:
                if real_max < sum_max:
                    real_max = sum_max
                recursive(idx + 1, max_val.append(boxess[idx][1]), boxes.append(boxess[idx]))

            # 1-6 높이 가로 세로
            if boxes[-1][2] >= boxess[idx][0] and boxes[-1][0] >= boxess[idx][1]:
                if real_max < sum_max:
                    real_max = sum_max
                recursive(idx + 1, max_val.append(boxess[idx][0]), boxes.append(boxess[idx]))

            ## 포함 안함
            bs[idx] = 0
            recursive(idx + 1, max_val, boxes)

    for i in range(len(boxess)):
        print('--------------------',i,'----------------')
        recursive(i, [0], [])
    print("#{} {}".format(tc, real_max))