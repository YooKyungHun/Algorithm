N, K = map(int, input().split())

lst = [[0, 0]]
for i in range(N):
    lst.append(list(map(int, input().split())))
    # [무게, 가치]
    # [[0, 0], [6, 13], [4, 8], [3, 6], [5, 12]]

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):  # i: 물건 개수
    for j in range(1, K+1):  # j: 무게

        # dp[4][7] = dp[3][7-지금 들 물건 무게] + 지금 들 물건 가치
        if j >= lst[i][0]:
            dp[i][j] = max(dp[i-1][j-lst[i][0]] + lst[i][1], dp[i-1][j])
        #
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])