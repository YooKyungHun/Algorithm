N = int(input())
lst = [0] * (N+1)
for i in range(1, N+1):
    lst[i] = int(input())
# [0, 6, 10, 13, 9, 8, 1]

# dp[n]: n 번째 포도주까지 주어졌을 때 최대값
dp = [0] * (N+1)
dp[1] = lst[1]

if N >= 2:
    dp[2] = dp[1] + lst[2]
if N >= 3:
    dp[3] = max(dp[2], lst[1]+lst[3], lst[2]+lst[3])
if N >= 4:
    for i in range(4, N+1):
        # 1) dp[i-1] 에 현재 포도주 마시지 않는 경우(dp[5] == dp[6])
        # 2) dp[i-2] 에 lst[i-1] 안마시고, 현재 포도주 마시는 경우
        # 3) dp[i-3] 에 lst[i-2] 안마시고, lst[i-1] 과 lst[i] 마시는 경우
        dp[i] = max(dp[i-1] + 0,
                    dp[i-2] + lst[i],
                    dp[i-3] + lst[i-1] + lst[i])

print(max(dp))