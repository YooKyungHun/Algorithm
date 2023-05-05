import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]+list(map(int, input().split())) for _ in range(N)]
# [[0, 1, 2, 3, 4], [0, 2, 3, 4, 5], [0, 3, 4, 5, 6], [0, 4, 5, 6, 7]]

arr.insert(0, [0] * (N+1))
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 3, 4, 5], [0, 3, 4, 5, 6], [0, 4, 5, 6, 7]]

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = arr[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
# [[0, 0, 0, 0, 0],
#  [0, 1, 3, 6, 10],
#  [0, 3, 8, 15, 24],
#  [0, 6, 15, 27, 42],
#  [0, 10, 24, 42, 64]]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])