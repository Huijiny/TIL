# 맨 앞글자가 원하는 단어로 시작하는지 확인하는 함수
def start_with(word, sentencce):
    word_len = len(word)
    if sentencce[:word_len] == word:
        return True
    return False


# rule과 그 다음으로 들어오는 values 에 대해서 처리하는 함수
def check(rule, value):
    if rule == 'STRING':
        if value.isalpha():
            return True
        return False
    if rule == 'NUMBER':
        if value.isdigit():
            return True
        return False


# flag rules를 dictionary 형태로 변환하여 반환하는 함수
def make_rule_dictionary(flag_rules):
    rule = {}
    # flag rule을 명령어에 따라 구분하여 dictionary에 저장
    for flag_rule in flag_rules:
        flag_name, option = flag_rule.split(' ')
        rule[flag_name] = option
    return rule


def solution(program, flag_rules, commands):
    answer = [True] * len(commands)

    # flag rule을 명령어에 따라 구분하여 dictionary에 저장
    rule = make_rule_dictionary(flag_rules)

    for command_index, command in enumerate(commands):
        # program name 판단
        if not start_with(program, command):
            answer[command_index] = False
            continue

        # command 판단
        written_flags = command[len(program):]
        written_flags_list = written_flags.split(" ")

        # 1-1) 프로그램명과 command 사이의 공백 존재 판단
        if not written_flags_list[0] == '':
            answer[command_index] = False
            continue

        # 1-2) 다음 명령어 판단
        idx = 1
        while idx != len(written_flags_list):
            flag_name = written_flags_list[idx]
            # 2-1) 명령어  앞에 - 포함 여부 판단
            if '-' == flag_name[:1]:
                value = rule[flag_name]

                # 3-1) NULL일 경우 다음 값 검사 x
                if value == 'NULL':
                    idx += 1

                # 3-2) String, Number일경우 check 함수 통해 판단.
                else:
                    if idx+1 <= len(written_flags_list):
                        if check(value, written_flags_list[idx+1]):
                            idx += 2
                        else:
                            answer[command_index] = False
                            break

            else:
                answer[command_index] = False
                break
    return answer

solution("line",["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"])