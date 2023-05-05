def solution(number, k):
    answer = ''
    cnt = 0
    N = len(number)

    while cnt != N - k:
        max_number = 0
        max_num_idx = 0
        end_idx = len(number) - (N - k - cnt)
        # 7 - 5 = 2
        # len(number) - 5 = 2
        # len(number) - (10 - 4 - cnt) = 2

        for i in range(0, end_idx + 1):
            if number[i] == '9':
                max_number = '9'
                max_num_idx = i
                break

            if max_number < int(number[i]):
                max_number = int(number[i])
                max_num_idx = i

        answer += str(max_number)
        number = number[max_num_idx + 1:]
        cnt += 1

    return answer

