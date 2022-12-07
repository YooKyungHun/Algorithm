import sys

R, C, K = map(int, input().split())

arr = [list(map(str, input())) for _ in range(R)]
# [['.', '.', '.', '.'], 
#  ['.', 'T', '.', '.'], 
#  ['.', '.', '.', '.']]

# 델타 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
def DFS(x, y, distance):
    global answer
    arr[x][y] = 'T'
    if [x, y] == [0, C-1]:
        # 거리가 K 이면 정답+1
        if distance == K:
            answer += 1
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != 'T':
            # 'T' 처리와 visited 배열을 이용한 방문처리와 같으므로 생략
            arr[nx][ny] = 'T'
            DFS(nx,ny,distance+1)
            arr[nx][ny] = 0

DFS(R-1, 0, 1)
print(answer)
