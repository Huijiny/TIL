# def f(number):
#     num_str = str(bin(number))[2:]
#     next_num = number + 1
#     num_str_lst = list(num_str)
#     num_int = list(map(int, num_str))
#     # print(all(num_int))
#     if all(num_int):
#         return int('0b10'+('1' * (len(num_str_lst)-1)), 2)
#     while True:
#         count = 0
#         next_num_str = str(bin(next_num))[2:]
#         # print(number, next_num)
#         # print(num_str, next_num_str)
#         for idx in range(1, len(num_str)+1):
#             # print(num_str[-idx], next_num_str[-idx])
#             if num_str[-idx] != next_num_str[-idx]:
#                 count += 1
#         # if len(num_str) < len(next_num_str):
#         #     count += 1
#         if count == 1:
#             # print(count)
#             break
#         next_num += 1
#
#     return next_num
# def f(number):
#     num_str = str(bin(number))[2:]
#     next_num = number + 1
#     num_str_lst = list(num_str)
#     num_int = list(map(int, num_str))
#     flag = True
#     # print(all(num_int))
#     if all(num_int):
#         return int('0b10'+('1' * (len(num_str_lst)-1)), 2)
#     while flag:
#         count = 0
#         next_num_str = str(bin(next_num))[2:]
#         # print(number, next_num)
#         # print(num_str, next_num_str)
#         for idx in range(1, len(num_str)+1):
#             # print(num_str[-idx], next_num_str[-idx])
#             if num_str[-idx] != next_num_str[-idx]:
#                 count += 1
#             if count > 2:
#                 break
#         # if len(num_str) < len(next_num_str):
#         #     count += 1
#         if count == 1 or count == 2:
#             # print(count)
#             break
#         next_num += 1
#
#     return next_num
# def f(number):
#     num_str = str(bin(number))[2:]
#     next_num = number + 1
#     num_str_lst = list(num_str)
#     num_int = list(map(int, num_str))
#     flag = True
#     if all(num_int):
#         return int('0b10'+('1' * (len(num_str_lst)-1)), 2)
#     while flag:
#         count = 0
#         next_num_str = str(bin(next_num))[2:]
#         for idx in range(1, len(num_str)+1):
#             if num_str[-idx] != next_num_str[-idx]:
#                 count += 1
#             if count > 2:
#                 break
#
#         if count == 1 or count == 2:
#             # print(count)
#             break
#         next_num += 1
#
#     return next_num
def f(number):
    num_str = str(bin(number))[2:]
    num_str_lst = list(num_str)
    num_int = list(map(int, num_str))
    # print(all(num_int))
    if all(num_int):
        return int('0b10'+('1' * (len(num_str_lst)-1)), 2)
    else:
        for i in range(len(num_str_lst)-1, -1, -1):
            # print(num_str_lst)
            # print(i)
            if num_str_lst[i] == '0':
                num_str_lst[i] = '1'
                new_num = '0b'+''.join(num_str_lst)
                return int(new_num, 2)


def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(f(number))
    print(answer)
    return answer
solution([2, 7])