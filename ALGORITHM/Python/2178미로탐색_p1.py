from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# [[1, 0, 1, 1, 1, 1],
#  [1, 0, 1, 0, 1, 0],
#  [1, 0, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1, 1]]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(a, b):
    queue = deque()
    queue.append([a, b])

    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1:
            return arr[x][y]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append([nx, ny])

    return

print(BFS(0, 0))