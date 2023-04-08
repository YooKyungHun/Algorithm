def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    if n >= 2:
        dp[2] = 3
    if n >= 4:
        for i in range(4, n + 1, 2):
            tmp = 0
            for j in range(0, i - 4 + 1, 2):
                tmp += dp[j]
            dp[i] += (dp[i - 2] * 3 + tmp * 2) % 1000000007

    return dp[n]
'''
# https://s2choco.tistory.com/24
# https://dev-note-97.tistory.com/182

# dp[2] = 3
# dp[4] = dp[2] * 3 + 2
# dp[6] = dp[4] * 3 + dp[2] * 2 + 2
# dp[8] = dp[6] * 3 + dp[4] * 2 + dp[2] * 2 + 2
# ...
# dp[n] = dp[n-2] * 3 + (dp[n-4] + dp[n-6] + dp[n-8] + ... + dp[2] + 1) * 2
#       = dp[n-2] * 3 + (dp[n-4] + dp[n-6] + dp[n-8] + ... + dp[2] + dp[0]) * 2
#       = dp[n-2] * 3 + (for j in range(0, n-4 + 1, 2):
#                            tmp += dp[j])
#       = dp[n-2] * 3 + tmp * 2
#       => = (dp[n-2] * 3 + tmp * 2) % 1000000007
'''