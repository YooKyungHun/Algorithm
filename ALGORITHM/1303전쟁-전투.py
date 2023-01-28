from collections import defaultdict

N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(M)]
# [['W', 'B', 'W', 'W', 'W'],
# ['W', 'W', 'W', 'W', 'W'],
# ['B', 'B', 'B', 'B', 'B'],
# ['B', 'B', 'B', 'W', 'W'],
# ['W', 'W', 'W', 'W', 'W']]

visited = [[0] * N for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def DFS(i, j, now):
    global team

    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]
        if 0 <= ni < M and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == now:
            visited[ni][nj] = 1
            team += 1
            DFS(ni, nj, arr[ni][nj])


answer = defaultdict(int)
for i in range(M):
    for j in range(N):
        # 완전탐색 할건데, visit 하지 않은 곳만
        if visited[i][j] == 0:
            # 현재 팀 수 1
            team = 1
            visited[i][j] = 1
            DFS(i, j, arr[i][j])
            answer[arr[i][j]] += team**2

# {'W': 130, 'B': 65})
print(answer['W'], answer['B'])