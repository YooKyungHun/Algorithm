from collections import deque

N, M = map(int, input().split())

arr = []
for i in range(M):
    arr.append(input())
# ['WBWWW',
#  'WWWWW',
#  'BBBBB',
#  'BBBWW',
#  'WWWWW']

visited = [[0] * N for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    team = arr[x][y]
    cnt_team = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == team:
                cnt_team += 1
                visited[nx][ny] = 1
                q.append((nx, ny))

    return cnt_team

answer = {'W': 0, 'B': 0}
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            visited[i][j] = 1
            answer[arr[i][j]] += BFS(i, j) ** 2

print(answer['W'], answer['B'])