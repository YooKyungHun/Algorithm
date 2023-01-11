from collections import deque
import sys
sys.setrecursionlimit(10**6)

M, N = map(int, input().split())

arr = [list(map(int, list(input()))) for _ in range(M)]
# [[0, 1, 0, 1, 0, 1],
# [0, 1, 0, 0, 0, 0],
# [0, 1, 1, 1, 0, 1],
# [1, 0, 0, 0, 1, 1],
# [0, 0, 1, 0, 1, 1]]

# 델타이동
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(a, b):
  global flag
  queue = deque()
  queue.append([a, b])
  visited[a][b] = 1

  while queue:
    x, y = queue.popleft()
    if x == M-1:
      flag = 1
      break

    for k in range(4):
      nx, ny = x + dx[k], y + dy[k]
      if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny] == 0:
        visited[nx][ny] = 1
        queue.append([nx, ny])

flag = 0  # NO
visited = [[0] * N for _ in range(M)]
# outer side 에서 0인 지점마다 visited 를 최신화할 필요는 없음
# 어차피 문제예시 (0, 2) 에서 시작해서 (0, 5) 도 방문하기 때문에
# (0, 5) 에서 전류를 주입해 볼 필요가 없는 거
for i in range(N):
  if arr[0][i] == 0 and visited[0][i] == 0: # 전류 주입
    BFS(0, i)

if flag == 1:
  print("YES")
else:
  print("NO")
