N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0]
dy = [0, 1]

def DFS(x, y, now):
    if arr[x][y] == -1:
        print("HaruHaru")
        exit(0)

    for k in range(2):
        nx, ny = x + now * dx[k], y + now * dy[k]

        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
            now = arr[nx][ny]
            DFS(nx, ny, now)
            now = arr[x][y]

DFS(0, 0, arr[0][0])
print("Hing")

# 3
# 1 0 2
# 0 1 2
# 2 1 -1

# 3
# 0 1 2
# 1 4 5
# 1 2 -1