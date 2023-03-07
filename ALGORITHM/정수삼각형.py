def solution(triangle):
    answer = 0
    n = len(triangle[-1])

    dp = [[0] * i for i in range(1, n + 1)]
    dp[0][0] = triangle[0][0]
    # dp = [[7], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]

    for i in range(1, n):
        for j in range(0, i + 1):

            # 각 row 의 첫 번째 dp 값 = 전 row 의 첫 번째 dp 값 + 각 row 의 현재 값
            if j == 0:
                dp[i][j] = dp[i - 1][0] + triangle[i][0]

            # 각 row 의 마지막 dp 값 = 전 row 의 마지막 dp 값 + 각 row 의 현재 값
            elif j == i:
                dp[i][j] = dp[i - 1][i - 1] + triangle[i][j]

            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    # dp = [[7],
    #       [10, 15],
    #       [18, 16, 15],
    #       [20, 25, 20, 19],
    #       [24, 30, 27, 26, 24]]

    return max(map(max, dp))

# dp[0] = 7
# dp[1] = 10, 15
# dp[2] = 18, 16, 15