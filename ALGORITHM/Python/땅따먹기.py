'''
solution2: 각 행마다 4 * 3 = 12 번씩 총 1,200,000 회 탐색
| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 8 | =>       / 1 + 6 / 1 + 7 / 1 + 8
                     2 + 5 /       / 2 + 7 / 2 + 8
                     3 + 5 / 3 + 6         / 3 + 8
                     5 + 5 / 5 + 6 / 5 + 7
| 4 | 3 | 2 | 1 |

solution1: 최대값과 prev(flag 개념) 을 이용해서 3 + 3 = 6 번씩 총 600,000 회 탐색
| 1 | 2 | 3 | 5 | => max = 5, prev = land[0].index(5) = 3, dk[prev] = [0, 1, 2]
| 5 | 6 | 7 | 8 | => 5 + 5 / 6 + 5 / 7 + 5 / max (1 + 8, 2 + 8, 3 + 8)
| 4 | 3 | 2 | 1 |

'''


def solution1(land):
    N = len(land)
    # dp[n][idx] : n 행에서 각 idx 를 선택했을 때 최대값

    # print(dp)
    # [[1, 2, 3, 5],
    # [10, 11, 12, 11],
    # [16, 15, 13, 13]]

    dp = [[0, 0, 0, 0] for _ in range(N)]
    dk = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]

    dp[0] = land[0]
    prev = land[0].index(max(dp[0]))  # 3
    for i in range(1, N):
        for j in range(4):
            if j in dk[prev]: # j: 3회
                dp[i][j] = land[i][j] + max(dp[i-1])

            else: # j: 1회
                for k in dk[prev]: # 0 1 2
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])

        prev = dp[i].index(max(dp[i]))

    return (max(map(max, dp)))


def solution2(land):
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

    dp[0] = [1, 2, 3, 5]

    dp[0] = land[0]  # [1, 2, 3, 5]
    for i in range(1, N):
        for j in range(4):  # 4번 반복
            for k in dk[j]:  # 3번 반복
                dp[i][j] = max(dp[i][j], land[i][j] + dp[i - 1][k])

    return (max(map(max, dp)))