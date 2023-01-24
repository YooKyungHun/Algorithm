"""
2차원 dp
굳이 디피테이블을 만들지 않아도 되면 만들지 말것.
n = 1일떄를 생각을 꼭해야됨!!
참고) https://beyond-common-sense.tistory.com/10
참고) https://pacific-ocean.tistory.com/197
"""

import sys
input = sys.stdin.readline

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    # N 이 외부 반복문, 2 가 내부 반복문
    for i in range(N):
        if i == 0: # 50, 30
            arr[0][0] = arr[0][0]
            arr[1][0] = arr[1][0]
        elif i == 1: # 10, 50
            arr[0][1] = arr[1][0] + arr[0][1]
            arr[1][1] = arr[0][0] + arr[1][1]
            # dp[0][1] = arr[1][0] + arr[0][1]
            # dp[1][1] = arr[0][0] + arr[1][1]
        else:
            arr[0][i] = max(arr[1][i-2], arr[1][i-1]) + arr[0][i]
            arr[1][i] = max(arr[0][i-2], arr[0][i-1]) + arr[1][i]
            # dp[0][2] = max(dp[1][0], dp[1][1]) + arr[0][2]
            # dp[1][2] = max(dp[0][0], dp[0][1]) + arr[1][2]

    # [[50, 40, 200, 140, 250],
    #  [30, 100, 120, 210, 260]]
    print(max(arr[0][N-1], arr[1][N-1]))



