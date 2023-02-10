def solution(land):
    answer = 0
    N = len(land)
    # dp[n][idx] : n 행에서 각 idx 를 선택했을 때 최대값
    # dp[1][0] = land[1][0] + max(          dp[0][1], dp[0][2], dp[0][3])
    # dp[1][1] = land[1][1] + max(dp[0][0],           dp[0][2], dp[0][3])
    # dp[1][2] = land[1][2] + max(dp[0][0], dp[0][1],           dp[0][3])
    # dp[1][3] = land[1][3] + max(dp[0][0], dp[0][1], dp[0][2])

    # print(dp) 
    # [[1, 2, 3, 5], 
    # [10, 11, 12, 11], 
    # [16, 15, 13, 13]]

    dp = [[0, 0, 0, 0] for _ in range(N)]
    dk = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]

    dp[0] = land[0]
    prev = land[0].index(max(dp[0])  # 3
    #     for i in range(1, N):
    #         for j in range(4):
    #             if j in dk[prev]: # j: 3회
    #                 dp[i][j] = land[i][j] + max(dp[i-1])

    #             else: # j: 1회
    #                 for k in dk[prev]: # 0 1 2
    #                     dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])

    #         prev = land[i].index(max(land[i]))

    return (max(map(max, dp)))