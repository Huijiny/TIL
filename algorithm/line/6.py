# 맨 앞글자가 원하는 단어로 시작하는지 확인하는 함
def start_with(word, sentencce):
    word_len = len(word)
    if sentencce[:word_len] == word:
        return True
    return False

# rule과 그 다음으로 들어오는 values 에 대해서 처리하는 함수
def check(rule, values):
    if rule == 'STRING':
        if len(values) == 1 and values[0].isalpha():
            return True
        return False

    if rule == 'STRINGS':
        for value in values:
            if not value.isalpha():
                return False
        return True
    if rule == 'NUMBER':
        if len(values) == 1 and values[0].isdigit():
            return True
        return False

    if rule == 'NUMBERS':
        for value in values:
            if not value.isdigit():
                return False
        return True

    if rule == 'NULL':
        if values == []:
            return True
        return False

# flag rules를 dictionary 형태로 변환하여 반환하는 함
def make_rule_dictionary(flag_rules):
    rule = {}
    # flag rule을 명령어에 따라 구분하여 dictionary에 저장
    for flag_rule in flag_rules:
        flag_name, option = flag_rule.split(' ')
        rule[flag_name] = option
    return rule

def solution(program, flag_rules, commands):

    answer = [True] * len(commands)
    rule = make_rule_dictionary(flag_rules)

    for command_index, command in enumerate(commands):
        # program name 판단
        if not start_with(program, command):
            answer[command_index] = False
            continue

        written_flags = command[len(program):]

        # 1-1) 프로그램명과 command 사이의 공백 존재 판단
        if not written_flags[:1] == ' ':
            answer[command_index] = False
            continue

        # 1-2) 명령어에 따른 arguments 조건 검사.
        #      while문의 idx 변수를 통해 -를 만나면 명령어 단위를 체크하여 check함수로 넘겨줌.
        idx = 1
        while idx <= len(written_flags):
            # 2-1) -를 기준으로 명령어 chunk divide
            if written_flags[idx] == '-':
                without_dash = written_flags[idx+1:]

                # 3-1) -가 중간에 나오는지, 또는 더이상 안나오는지 에 따라서 one_line변수에 명령어 chunk 할당
                if without_dash.find('-') != -1:
                    one_line = '-' + without_dash[:without_dash.find('-')]
                    one_line = one_line.rstrip()
                    idx = without_dash.find('-') + idx + 1

                # 3-2) -가 더이상 나오지 않는다면.
                else:
                    one_line = written_flags[idx:]
                    idx = len(written_flags) + 1

                # 3-3) 명령어 chunk를 기준으로 flag_name과 그에 따른 arguments로 divide
                words = str(one_line).split(" ")
                flag_name = words[0]
                arguments = words[1:]

                # 3-4) check 함수를 통해 올바른 arguments인지 판단.
                if not check(rule[flag_name], arguments):
                    answer[command_index] = False

            else:
                answer[command_index] = False
                break
    return answer

solution("trip",["-days NUMBERS", "-dest STRING"],["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"])