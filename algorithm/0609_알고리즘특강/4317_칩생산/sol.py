import sys
sys.stdin = open('sample_sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    result = 0

    h, w = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(h)]
    for col in range(h):
        for row in range(w):
            if area[col][row] == 0:
                if 0 <= col+1 < h and 0 <= row+1 < w and area[col][row+1] == 0 and area[col+1][row] == 0 and area[col+1][row+1] == 0:
                    area[col][row] = 1
                    area[col][row+1] = 1
                    area[col+1][row] = 1
                    area[col+1][row+1] = 1
                    result += 1


    print("#{} {}".format(tc, result))