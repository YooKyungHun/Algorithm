N = int(input())
lst = [int(input()) for _ in range(N)]
lst = [0] + lst

dp = [0] * (N+1)

dp[1] = lst[1]
if N >= 2:
    dp[2] = dp[1] + lst[2]
if N >= 3:
    dp[3] = max(lst[2] + lst[3], lst[1] + lst[3])
if N >= 4:
    for i in range(4, N+1):
        dp[i] = max(dp[i-3] + 0 + lst[i-1] + lst[i], dp[i-2] + 0 + lst[i])
print(dp[-1])
#
# 10
# 3
# 5
# 10
# 9
# 2
# 1
# 2
# 5
# 2
# 9
# [0, 3, 8, 15, 22, 19, 23, 25, 28, 30, 37]

