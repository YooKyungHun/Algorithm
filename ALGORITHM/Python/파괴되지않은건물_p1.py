from collections import defaultdict


def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])

    accumulated = [[0] * (M + 1) for _ in range(N + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: degree *= -1

        accumulated[r1][c1] += degree
        accumulated[r1][c2 + 1] -= degree
        accumulated[r2 + 1][c1] -= degree
        accumulated[r2 + 1][c2 + 1] += degree

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

    for i in range(0, N + 1):
        for j in range(1, M + 1):
            accumulated[i][j] += accumulated[i][j - 1]

    for i in range(1, N + 1):
        for j in range(0, M + 1):
            accumulated[i][j] += accumulated[i - 1][j]

    for i in range(N):
        for j in range(M):
            accumulated[i][j] += board[i][j]
            if accumulated[i][j] >= 1:
                answer += 1

    return answer

# 3  0 -3      3  3  0      3  3  0
# 0  0  0      0  0  0      3  3  0
# 0  0  0      0  0  0      3  3  0
# -3 0  3      -3 -3 0      0  0  0