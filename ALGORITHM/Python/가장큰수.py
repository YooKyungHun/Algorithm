def solution(numbers):
    answer = ''

    full_num = []

    for i in range(len(numbers)):
        number = numbers[i]
        number = str(number)
        full_num.append([len(number)])

        while len(number) < 4:
            number += number
        number = number[0:4]
        full_num[i].append(number)

    # full_num = [[3, '3333'], [2, '3030'], [2, '3434'], [3, '5555'], [3, '9999']]

    full_num.sort(key=lambda x: x[1], reverse=True)
    # full_num = [[3, '9999'], [3, '5555'], [2, '3434'], [3, '3333'], [2, '3030']]

    for num in full_num:
        origin_length, number = num[0], num[1]
        answer = answer + number[0:origin_length]

    if int(answer) == 0:
        return "0"
    return answer

    # 30 34 3 => 30 34 33 => 34 3 30
    # 30 34 3 => 3030 3434 3333 => 3434 + 3333 + 3030 => 3434[0:2] + 3333[0:1] + 3030[0:2]
