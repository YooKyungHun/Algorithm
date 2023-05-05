N = int(input())
lst = list(map(int, input().split()))
lst.insert(0, 0)
# lst = [0, 1, 5, 6, 7]

# dp[n]: n 개의 카드를 갖기 위한 최대값
# ex) dp[3] 은 dp[2] 에 1개만 더하든지, dp[1] 에 2개를 더하든지, 3개짜리만 사든지

dp = [0] * (N+1)
dp[1] = lst[1]

for i in range(2, N+1):
    for j in range(i):
        dp[i] = max(dp[0 + j] + lst[i - j], dp[i])

print(dp[N])
    # dp[2] = dp[0] + lst[2] or
    #         dp[1] + lst[1]
    # dp[3] = dp[0] + lst[3] or
    #         dp[1] + lst[2] or
    #         dp[2] + lst[1]
    #
    # dp[4] = dp
