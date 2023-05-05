import sys
sys.setrecursionlimit(10**6)

N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
# [['R', 'R', 'R', 'B', 'B'],
# ['G', 'G', 'B', 'B', 'B'],
# ['B', 'B', 'B', 'R', 'R'],
# ['B', 'B', 'R', 'R', 'R'],
# ['R', 'R', 'R', 'R', 'R']]

# 델타 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global visited, arr
    visited[x][y] = 1

    color = arr[x][y]
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < N and 0 <= ny < N:
            if color == arr[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                DFS(nx, ny)
                # visited[nx][ny] = 0

# 1) 비색약
cnt = 0
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 방문하지 않은 점에 대해서만 DFS
        if visited[i][j] == 0:
            DFS(i, j)
            cnt += 1
print(cnt, end=' ')

# 2) 색약
cnt = 0
visited = [[0]*N for _ in range(N)]
# 2-1) 색약이니까 R 과 G 를 동일하게 만들기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

for i in range(N):
    for j in range(N):
        # 방문하지 않은 점에 대해서만 DFS
        if visited[i][j] == 0:
            DFS(i, j)
            cnt += 1
print(cnt)
