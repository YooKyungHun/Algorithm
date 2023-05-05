N = int(input())
lst = [0] + list(map(int, input().split()))

dp = [0] + [float('inf')] * (N)

dp[1] = lst[1]
for i in range(2, N+1):
    for j in range(i):
        dp[i] = min(dp[j] + lst[i-j], dp[i])
# dp[1] = lst[1]
# dp[2] = min(lst[1] + dp[1],   // => min(lst[1] + dp[1], dp[2])
#             lst[2] + dp[0])   // => min(lst[2] + dp[0], dp[2])
# dp[3] = min(lst[1] + dp[2],   // => min(lst[1] + dp[2], dp[3])
#             lst[2] + dp[1],   // => min(lst[2] + dp[1], dp[3])
#             lst[3] + dp[0])   // => min(lst[3] + dp[0], dp[3])
# dp[4] = min(lst[1] + dp[3],
#             lst[2] + dp[2],
#             lst[3] + dp[1],
#             lst[4] + dp[0])
print(dp[-1])