# 평균을 내는 함수!
# def _avg(scores):
#     try:
#         return sum(scores) / len(scores)
#     except ZeroDivisionError:
#         return 0

class NoTestError(ZeroDivisionError):
    pass

def _avg(scores):
    if len(scores) == 0:
        raise NoTestError('시험안본 학생이 있습니다.')
    return sum(scores)/len(scores)
    
# 위의 함수를 활용해서 학생들의 각각 평균을 내는 함수
def class_avg(students):
    for scores in students.values():
        print(_avg(scores))
