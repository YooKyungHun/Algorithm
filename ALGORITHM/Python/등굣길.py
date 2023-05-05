def solution(m, n, puddles):
    answer = 0

    lst = [[1] * m for _ in range(n)]

    for puddle in puddles:
        y, x = puddle
        lst[x - 1][y - 1] = 0

    for i in range(1, n):
        lst[i][0] = min(lst[i - 1][0], lst[i][0])

    for j in range(1, m):
        lst[0][j] = min(lst[0][j - 1], lst[0][j])

    for i in range(1, n):
        for j in range(1, m):
            if lst[i][j]:
                lst[i][j] = (lst[i - 1][j] + lst[i][j - 1]) % 1_000_000_007

    return lst[-1][-1]