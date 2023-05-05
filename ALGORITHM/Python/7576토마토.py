from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

tomato = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append((i, j))
tomato = deque(tomato)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while tomato:
    x, y = tomato.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            arr[nx][ny] = arr[x][y] + 1
            tomato.append((nx, ny))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            exit(0)  # 코드 강제 종료
print(max(map(max, arr))-1)  # 2차원 배열의 최대값



