definition = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
              '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}


def find_code(codes):
    for i in range(N):
        for j in range(M-1, -1, -1):
            if codes[i][j] == '1':
                code = codes[i][j-55:j+1]
                return code
T = int(input())

for tc in range(1, T+1):
    result = 0
    N, M = map(int, input().split())
    codes = [input()for _ in range(N)]
    code = find_code(codes)
    letter = ''
    start = 0
    end = start + 7
    for i in range(8):
        letter += definition[code[start:end]]
        start += 7
        end = start + 7
    letter = list(map(int, letter))
    result = (letter[0]+letter[2]+letter[4]+letter[6])*3 + (letter[1]+letter[3]+letter[5]) + letter[7]
    if result % 10 != 0:
        result = 0
    else:
        result = sum(letter)
    print("#{} {}".format(tc, result))