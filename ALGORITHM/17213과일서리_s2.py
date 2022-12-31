# 과일의 종류 수 N(1 ≤ N ≤ 10)
N = int(input())
# 훔치려 하는 과일의 개수 M(N ≤ M ≤ 30)
M = int(input())

# dp[N][M]
dp = [[0] * (31) for _ in range(31)]

for i in range(1, N+1):
    for j in range(i, M+1):

        if i == 1:
            dp[1][j] = 1

        else: # N = 2, 3, 4, 5 ,,,,
            for k in range(i-1, j):
                dp[i][j] += dp[i-1][k]

print(dp[N][M])

# N M
# 1 이면 M 에 상관없이 1
# 2 2 1
#   3 2
#   4 3
#   5 4
#   6 5
# 3 3 1
#   4 3
#   5 6
#   6 10
#   7 15
#   8 21
# 4 4 1
#   5 4
#   6 10
#   7 20
#   8 35
#   9 56
