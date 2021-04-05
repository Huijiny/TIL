def solution(inp_str):
    answer = []
    capital = list(range(ord('A'), ord('Z')+1))
    small = list(range(ord('a'), ord('z')+1))
    number = list(map(str, range(10)))
    special = ['~','!','@','#','$','%','^','&','*']
    including_check = [0, 0, 0, 0]

    if not 8 <= len(inp_str) <= 15:
        answer.append(1)

    for i in inp_str:
        if ord(i) in capital or ord(i) in small or i in number or i in special:
            continue
        else:
            answer.append(2)
            break

    for i in inp_str:
        if sum(including_check) >= 3:
            break
        if ord(i) in capital:
            including_check[0] = 1
        elif ord(i) in small:
            including_check[1] = 1
        elif i in number:
            including_check[2] = 1
        elif i in special:
            including_check[3] = 1
    if sum(including_check) < 3:
        answer.append(3)

    if len(inp_str) >= 4:
        for idx in range(len(inp_str)-3):
            tmp_str = inp_str[idx:idx+4]
            if len(set(tmp_str)) == 1:
                answer.append(4)
                break

    for i in inp_str:
        if len(inp_str) - len(inp_str.replace(i, '')) >= 5:
            answer.append(5)
            break

    if len(answer) == 0:
        answer.append(0)
    return answer
print(solution("ZzZz)))))"))