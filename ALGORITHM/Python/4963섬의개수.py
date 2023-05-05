import sys
sys.setrecursionlimit(10**9)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def DFS(x, y):

    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]

        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            DFS(nx, ny)

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        exit(0)
    arr = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                answer += 1
                DFS(i, j)

    print(answer)