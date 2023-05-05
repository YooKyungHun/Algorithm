from collections import deque

TC = int(input())

# 델타이동
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 1 1 1 / 1 1 5
# (x1, y1) 에서 거리가 1인 점 -> (2, 1), (1, 2), (0, 1), (1, 0)
# 4개의 점 중에서 (x2, y2) 까지의 거리가 5인 좌표의 개수

# -10000 -9999 -9998 ... -2 -1 0 1 2 ... 9999 10000
# 0 1 2 ...9998 9999 10000 10001 10002 ... 19999 20000  

visited = [[0] * 20001 for _ in range(20001)]

for tc in range(TC):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  x1, y1, x2, y2 = x1+10000, y1+10000, x2+10000, y2+10000
  BFS(x1, y1)

def BFS(a, b):
  q = deque([])
  q.append((a, b))
  visited[a, b] = 1

  while q:
    x, y = q.popleft()
    cnt += 1

    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      if -10000<= nx <= 10000 and -10000<= ny <= 10000:
        if visited[nx, ny] == 0:
          q.append(nx, ny)
          visited[nx, ny] = 1
      

