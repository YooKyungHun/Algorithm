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

def DFS(x, y):
  # 종료조건
  global flag

  if x == M-1 and arr[x][y] == 0:
    flag = 1  # YES
    # print("종료조건 안쪽", x, y)
    return
  
  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]

    if 0 <= nx < M and 0 <= ny < N:
      if arr[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        DFS(nx, ny)
        visited[nx][ny] = 0
      

flag = 0  # NO
for i in range(N):
  if arr[0][i] == 0: # 전류 주입
    visited = [[0] * N for _ in range(M)]
    DFS(0, i)

if flag == 1:
  print("YES")
else: 
  print("NO")




