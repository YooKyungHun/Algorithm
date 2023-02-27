from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# [[0, 1, 1, 0, 1, 0, 0],
#  [0, 1, 1, 0, 1, 0, 1],
#  [1, 1, 1, 0, 1, 0, 1],
#  [0, 0, 0, 0, 1, 1, 1],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 1, 1, 0],
#  [0, 1, 1, 1, 0, 0, 0]]

visited = [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                queue.append([nx, ny])

    return cnt

BFS_count = 0
answer = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            BFS_count += 1
            number = arr[i][j]
            answer.append(BFS(i, j))

print(BFS_count)
answer.sort()
print(*answer, sep='\n')

