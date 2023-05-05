N, M = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j != 0:
            arr[i][j] += arr[i][j-1]
        if i != 0 and j == 0:
            arr[i][j] += arr[i-1][j]
        if i != 0 and j != 0:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1]) + arr[i][j]

print(max(map(max, arr)))