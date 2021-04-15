import sys
sys.stdin = open("sample_input (3).txt")
hex = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

decryption = {
    '211': 0, '221': 1, '122': 2, '411': 3, '132': 4,
    '231': 5, '114': 6, '312': 7, '213': 8, '112': 9
}


def is_valid(letter):
    result = (letter[0] + letter[2] + letter[4] + letter[6]) * 3 + (letter[1] + letter[3] + letter[5]) + letter[7]
    if result % 10 != 0:
        return False
    else:
        return True


def change_hex_to_bin(code):
    for n in range(N):
        bin_numb = ''
        for c in code[n]:
            bin_numb += hex[c]
        code[n] = bin_numb
    return code


T = int(input())

for tc in range(1, 1+T):
    result = 0
    valid_code = []
    N, M = map(int, input().split())
    code = [input()[:M] for _ in range(N)]
    # 각 줄의 바코드를 2진수로 모두 변환작업
    change_hex_to_bin(code)

    password = []
    for i in range(N):
        co1, co2, co3 = 0, 0, 0
        if '1' not in code[i]:
            continue
        for j in range(M*4-1, -1, -1):
            if co2 == 0 and co3 == 0 and code[i][j] == '1':
                co1 += 1
            elif co1 and co3 == 0 and code[i][j] == '0':
                co2 += 1
            elif co1 and co2 and code[i][j] == '1':
                co3 += 1
            elif co3 and code[i][j] == '0':
                standard = min(co1, co2, co3)
                tmp = str(co3//standard) + str(co2//standard) + str(co1//standard)
                password.append(decryption.get(tmp))
                co1 = co2 = co3 = 0
                if len(password) == 8:
                    password.reverse()
                    if password not in valid_code and is_valid(password):
                        result += sum(password)
                        valid_code.append(password)
                    password = []
    print("#{} {}".format(tc, result))