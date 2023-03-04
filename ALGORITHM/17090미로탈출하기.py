from sys import setrecursionlimit, stdin

input = stdin.readline
setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

dic = {'U': [-1, 0], 'R': [0, 1], 'D': [1, 0], 'L': [0, -1]}
dp = [[-1] * M for _ in range(N)]
# -1 안가봄 # 0 탈출불가 # 1 탈출가능


def DFS(x, y):
    # 탈출하게 된다면
    if not (0 <= x < N and 0 <= y < M):
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dx, dy = dic[arr[x][y]]
    nx, ny = x + dx, y + dy

    dp[x][y] = DFS(nx, ny)

    return dp[x][y]

for i in range(N):
    for j in range(M):
        if dp[i][j] == -1:
            DFS(i, j)
print(dp)