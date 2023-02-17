from collections import defaultdict

def solution(board, skill):
    N, M = len(board), len(board[0])

    tmp = [[0] * M for _ in range(N)]
    # 0, 0, 2, 3 => (0, 0) ~ (2, 3)
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= (-1)

        tmp[r1][c1] += degree
        if c2 + 1 <= M - 1:                 tmp[r1][c2 + 1] -= degree
        if r2 + 1 <= N - 1:                 tmp[r2 + 1][c1] -= degree
        if r2 + 1 <= N - 1 and c2 + 1 <= M - 1: tmp[r2 + 1][c2 + 1] += degree

    #    누적합 구할때 가로나 세로를 먼저 구하고,
    #    나머지 누적합을 구할 것
    #     [a, b, c]
    #     [d, e, f]

    #     [a, a+b, a+b+c]
    #     [d, d+e, d+e+f]

    #     올바른 누적합
    #     [a, a+b, a+b+c]
    #     [a+d, a+b+d+e, a+b+c+d+e+f]

    #     올바르지 못한 누적합
    #     [a, a+b, a+b+c]
    #     [a+d, a+b+e, a+a+a+b+b+c+d+e]

    for i in range(1, N):
        for j in range(0, M):
            tmp[i][j] += tmp[i - 1][j]
    for i in range(0, N):
        for j in range(1, M):
            tmp[i][j] += tmp[i][j - 1]

    answer = 0
    for i in range(N):
        for j in range(M):
            tmp[i][j] += board[i][j]
            if tmp[i][j] >= 1:
                answer += 1
    return answer