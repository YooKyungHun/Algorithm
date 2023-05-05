N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):

        if i == 1:
            dp[i][j] = j
        if j == 1:
            dp[i][j] = 1
        if i >= 2 and j >= 2:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_000

print(dp[N][K])

# N\K 0 1 2 3 4 5 6 7
# 0
# 1     1 2 3 4 5 6 7
# 2     1 3 6
# 3     1 4
# 4     1
# 5     1
# 6     1
# 7     1