def solution(left, right):
    answer = 0
    numbers = range(left, right+1)
    for number in numbers:
        count = 0
        for i in range(1, number+1):
            if number % i == 0:
                count += 1
        if count % 2 == 0:
            answer += number
        else:
            answer -= number
    return answer