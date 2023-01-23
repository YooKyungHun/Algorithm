from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N * H)]

# 델타 좌 우 위 아래 하 상
dx1 = [0, 0, N, -N, 1, -1]
dy1 = [-1, 1, 0, 0, 0, 0]

# 델타 좌 우 위 아래 상
dx2 = [0, 0, N, -N, -1, 0]
dy2 = [-1, 1, 0, 0, 0, 0]

# 델타 좌 우 위 아래 하
dx3 = [0, 0, N, -N, 1, 0]
dy3 = [-1, 1, 0, 0, 0, 0]

queue = deque()

for i in range(N * H):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()

    # 델타이동
    for k in range(6):
        nx = x + dx2[k] if x % N == N-1 else x + dx3[k] if x % N == 0 else x + dx1[k]
        ny = y + dy2[k] if x % N == N-1 else y + dy3[k] if x % N == 0 else y + dy1[k]

        # time 이나 거리의 경우 (+1) 을 통해
        # 변수를 생략할 수 있는 경우가 많음
        if 0 <= nx < N * H and 0 <= ny < M and arr[nx][ny] == 0:
            arr[nx][ny] = arr[x][y] + 1
            queue.append([nx, ny])

for i in range(N * H):
    for j in range(M):
        # 익지 않은 토마토가 남아있다면
        if arr[i][j] == 0:
            print(-1)
            exit(0)

# 모든 토마토가 남아있다면
# 2차원 배열의 최대값 -1  출력
print(max(map(max, arr)) - 1)

# out 3
# 5 5 2
# 1 -1 1 -1 1
# 0 0 -1 -1 1
# 0 -1 -1 1 0
# 0 -1 0 0 1
# 0 0 1 -1 1
# 1 -1 -1 -1 -1
# 0 -1 0 1 1
# 0 1 0 0 -1
# -1 -1 -1 -1 -1
# -1 0 0 1 -1



