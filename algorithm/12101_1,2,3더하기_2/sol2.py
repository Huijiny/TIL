n, k = map(int, input().split())

def makesik(numbers):
    answer = ''
    for number in numbers:
        answer += str(number) + '+'
    return answer[:len(answer)-1]

def backtrack(num, numbers):
    global answers

    if num == n:
        answers.append(makesik(numbers))
        return
    elif num > n:
        return
    else:
        backtrack(num + 1, numbers+[1])
        backtrack(num + 2, numbers+[2])
        backtrack(num + 3, numbers+[3])

arr = [1, 2, 3]
numbers = [0]
answers = []

for a in arr:
    numbers[0] = a
    backtrack(a, numbers)

answers.sort()
if len(answers) < k:
    print(-1)
else:
    print(sorted(answers)[k-1])