N = int(input())
lst = list(map(int, input().split()))
lst.insert(0, 0)
# lst = [0, 1, 5, 6, 7]

# dp[n]: n 개의 카드를 갖기 위한 최대값
# ex) dp[3] 은 dp[2] 에 1개만 더하든지, dp[1] 에 2개를 더하든지, 3개짜리만 사든지

dp = [0 for _ in range(N+1)]
# dp[1] = lst[1]
# dp[2] = max(lst[1] + dp[1],   // => max(lst[1] + dp[1], dp[2])
#             lst[2] + dp[0])   // => max(lst[2] + dp[0], dp[2])
# dp[3] = max(lst[1] + dp[2],   // => max(lst[1] + dp[2], dp[3])
#             lst[2] + dp[1],   // => max(lst[2] + dp[1], dp[3])
#             lst[3] + dp[0])   // => max(lst[3] + dp[0], dp[3])
# dp[4] = max(lst[1] + dp[3],
#             lst[2] + dp[2],
#             lst[3] + dp[1],
#             lst[4] + dp[0])

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(lst[j] + dp[i - j], dp[i])

print(dp[N])


# max 를 한번만 사용하면 좋겠지만, 여러번 사용해야 하므로
# 최신화 시키는 방법으로 하면 시간단축가능
# if dp[i] < (lst[j] + dp[i - j]):
#     dp[i] = (lst[j] + dp[i - j])