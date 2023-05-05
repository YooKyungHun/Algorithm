def solution(data, col, row_begin, row_end):
    tmp = []
    N = len(data)
    M = len(data[0])

    data.sort(key=lambda x: (x[col - 1], -x[0]))
    # data = [[4, 2, 9], [2, 2, 6], [1, 5, 10], [3, 8, 3]]

    for i in range(row_begin - 1, row_end - 1 + 1):
        sum_low = 0
        for j in range(M):
            sum_low += data[i][j] % (i + 1)
        tmp.append(sum_low)
    # data = [[4, 2, 9], [0, 0, 0], [1, 2, 1], [3, 8, 3]]
    # tmp = [0, 4]

    answer = 0
    for i in tmp:
        answer ^= i

    return answer