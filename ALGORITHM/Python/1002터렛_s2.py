from collections import deque

# TC = int(input())

# 델타이동
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * 20001 for _ in range(20001)]
lst = []
cnt = 0

def DFS(x, y):
  global cnt 
  if cnt == r1:
    lst.append([x, y])
    return 

  for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]

    if -10000<= nx <= 10000 and -10000<= ny <= 10000:
      if visited[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt += 1
        DFS(nx, ny)
        visited[nx][ny] = 0
        cnt -= 1

# for tc in range(TC):
x1, y1, r1, x2, y2, r2 = map(int, input().split())
x1, y1, x2, y2 = x1+10000, y1+10000, x2+10000, y2+10000
DFS(x1, y1)


print(lst)
