from collections import deque

N, M = map(int, input().split())
arr = list(list(input()) for _ in range(N))
visited = [[0] * M for _ in range(N)]
# [['1', '0', '1', '1', '1', '1'],
#  ['1', '0', '1', '0', '1', '0'],
#  ['1', '0', '1', '0', '1', '1'],
#  ['1', '1', '1', '0', '1', '1']]
# N, M = N - 1, M - 1
# 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(a, b):
    queue = deque()
    queue.append([a, b])
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1:
            break

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '1':
                # A 지점에서 B 지점으로 가는 거리를 더하는거라 cnt 를 쓸 필요 없음
                # 또한 arr 가 1 과 0 으로 이루어져 있어서 visited 를 대체가능
                arr[nx][ny] = int(arr[x][y]) + 1
                queue.append([nx, ny])

    return arr[-1][-1]

print(BFS(0, 0))
