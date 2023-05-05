from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS():
    queue = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                queue.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1

BFS()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            exit(0)
print(max(map(max, arr)) -1)