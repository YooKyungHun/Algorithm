N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j == 1:
            dp[i][j] = 1
        elif i == 1:
            dp[i][j] = j
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

'''
N / K 1  2  3  4  5
  1   1  2  3  4
  2   1  3  6  10
  3   1  4  10 20
  4   1  5  15 35
  5   1  6  21 54
'''


print(dp[N][K])

