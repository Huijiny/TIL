d = {
    ')': '(',
    '}': '{',
    ']': '['
}
def ispair(s):
    stack = []
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if stack:
                top = stack.pop()
                if d[c] != top:
                    # 만약 여는괄호, 닫는괄호 틀렸으면 이 s는 끝. 나와.
                    return False
            else:
                return False
    # for 끝났는데 stack 비어있으면 ok
    if len(stack) == 0:
        return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        tmp_s = s[i:] + s[0:i]
        if ispair(tmp_s):
            answer += 1

    return answer


print(solution("}}}"))
