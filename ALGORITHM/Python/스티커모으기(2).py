def solution(st):
    answer = 0
    N = len(st)

    dp = [0] * (N + 1)
    dp[0] = 0

    dp2 = [0] * (N + 1)
    dp2[0] = 0

    # 맨 앞에 뗐다고 쳐
    # 14                  => dp[1] = st[0]
    # 14 6                => dp[2] = dp[1]
    # 14 6 5              => dp[3] = dp[2]
    # 14 6 5 11           => dp[4] = max(dp[3], dp[2] + st[2])
    # 14 6 5 11 3         => dp[5] = max(dp[4], dp[3] + st[3])
    # 14 6 5 11 3 9       => dp[6] = max(dp[5], dp[4] + st[4])
    # 14 6 5 11 3 9 2     => ...
    # 14 6 5 11 3 9 2 10  => ...
    for i in range(1, N + 1):
        if i == 1:
            dp[i] = st[0]
        elif i == 2:
            dp[i] = st[0]
        elif i == 3:
            dp[i] = st[0]
        elif i >= 4:
            dp[i] = max(dp[i - 1], dp[i - 2] + st[i - 2])

    # 맨 앞에 안 뗐다고 쳐
    # 14                  => dp[1] = X
    # 14 6                => dp[2] = st[1]
    # 14 6 5              => dp[3] = max(dp[2], dp[1] + st[2])
    # 14 6 5 11           => dp[4] = max(dp[3], dp[2] + st[3])
    # 14 6 5 11 3         => dp[5] = max(dp[4], dp[2] + st[4])
    # 14 6 5 11 3 9       => dp[6] = max(dp[5], dp[3] + st[5])
    # 14 6 5 11 3 9 2     => ...
    # 14 6 5 11 3 9 2 10  => ...
    if N >= 2:
        for i in range(2, N + 1):
            if i == 2:
                dp2[i] = st[1]
            elif i == 3:
                dp2[i] = max(dp2[i - 1], st[2])
            else:
                dp2[i] = max(dp2[i - 1], dp2[i - 2] + st[i - 1])

    return (max(max(dp), max(dp2)))