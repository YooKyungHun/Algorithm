N, M = map(int, input().split())
K = int(input())

ABCD = []
for i in range(K):
    a, b, c, d = map(int, input().split())

    ABCD.append([a, b, c, d])

dp = [[0] * (M+1) for _ in range(N+1)]

# 맨 윗줄 초기세팅
for j in range(1, M+1):
    # 도로가 막혀있다면 그 이후로는 모두 0
    if [0, j-1, 0, j] in ABCD or [0, j, 0, j-1] in ABCD:
        dp[0][j] = 0
        break
    else:
        dp[0][j] = 1

# 맨 왼쪽줄 초기세팅
for i in range(1, N+1):
    # 도로가 막혀있다면 그 이후로는 모두 0
    if [i-1, 0, i, 0] in ABCD or [i, 0, i-1, 0] in ABCD:
        dp[i][0] = 0
        break
    else:
        dp[i][0] = 1

dp[0][0] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        # 왼쪽과 위쪽 모두로 부터 길이 막힌 경우
        if ([i, j-1, i, j] in ABCD or [i, j, i, j-1] in ABCD) and ([i - 1, j, i, j] in ABCD or [i, j, i - 1, j] in ABCD):
            dp[i][j] = 0

        # 왼쪽으로부터 길이 막힌 경우(왼쪽 -- x --> 오른쪽)
        elif [i, j-1, i, j] in ABCD or [i, j, i, j-1] in ABCD:
            dp[i][j] = dp[i-1][j]

        # 위쪽으로부터 길이 막힌 경우(위쪽 -- x --> 아래쪽)
        elif [i-1, j, i, j] in ABCD or [i, j, i-1, j] in ABCD:
            dp[i][j] = dp[i][j-1]

        # 길이 막히지 않은 경우
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])
