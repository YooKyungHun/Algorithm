from collections import deque

TC = int(input())

def BFS(x, y, a, b, cnt):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        # 종료조건
        if x == a and y == b:
            break

        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                # A 지점에서 B 지점으로 가는 횟수를 세는거라 cnt 를 쓸 필요 없음
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    print(visited[a][b])

for tc in range(1, TC+1):
    l = int(input())
    # 현재위치
    x, y = map(int, input().split())
    # 목표위치
    a, b = map(int, input().split())

    visited = list([0] * l for _ in range(l))
    visited[x][y] = 0

    # 1시부터 시계방향
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    cnt = -1

    BFS(x, y, a, b, cnt)


