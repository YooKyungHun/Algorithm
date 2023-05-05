N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

dp = [[0] * (i+1) for i in range(N)]
# [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]

if N > 1:
    dp[0][0] = arr[0][0]
    dp[1][0] = dp[0][0] + arr[1][0]
    dp[1][1] = dp[0][0] + arr[1][1]
    for i in range(2, N):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][0] + arr[i][0]
            if j != 0 and j != i:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]
            if j == i:
                dp[i][j] = dp[i-1][j-1] + arr[i][j]

    print(max(map(max, dp)))
elif N == 1:
    print(arr[0][0])


# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
# 맨 왼쪽값(dp[i][0])과 오른쪽값(dp[i][j])은
# 직전 dp 의 맨 왼쪽값(dp[i-1][0]) 과 맨 오른쪽 값(dp[i-1][j-1]) 에
# 현재값 (arr[i][0], arr[i][j]) 더한것
#
# 가운데 값들은 직전 dp 값 둘 중에 더 큰것에 현재값 더한것
# ex) dp[4][2] = max(dp[3][1], dp[3][2]) + arr[4][2]