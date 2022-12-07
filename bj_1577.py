N, M = map(int, input().split())
K = int(input())
arr = [([0]*(M+1)) for _ in range(N+1)]
visited = [([0]*(M+1)) for _ in range((N+1))]

# 현재위치
x = 0
y = 0

# 델타이동 (오른쪽, 위)
dx = [1, 0]
dy = [0, 1]

roads = []
for k in range(K):
  a, b, c, d = map(int, input().split())
  roads.append((a,b,c,d))

cnt = 0
def DFS(x, y):
  global cnt
  if x == N and y == M:
    cnt += 1
  else:
    for a,b,c,d in roads:
      for l in range(2):
        nx = x + dx[l]
        ny = y + dy[l]
        if 0 <= nx <=N and 0 <= ny <= M and visited[nx][ny] == 0:
          # 기존의 길 
          # (a, b) -> (c, d)
          # (c, d) -> (a, b)
          if (x == a and y == b and nx == c and ny == d) or (x == c and y == d and nx == a and ny == b):
            break
          else:
            visited[nx][ny] = 1
            DFS(nx, ny)
            visited[nx][ny] = 0
DFS(x, y)
print(cnt)