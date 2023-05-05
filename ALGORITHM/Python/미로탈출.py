from collections import deque


def BFS(S, E, visited, N, M, maps):
    queue = deque()
    start_x, start_y = S[0][0], S[0][1]
    end_x, end_y = E[0][0], E[0][1]

    queue.append([start_x, start_y])
    visited[start_x][start_y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return visited[end_x][end_y] - 1

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return -1


def solution(maps):
    answer = 0
    N, M = len(maps), len(maps[0])
    visited = [[0] * M for _ in range(N)]
    S = []
    E = []
    L = []

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                S.append([i, j])
            elif maps[i][j] == 'E':
                E.append([i, j])
            elif maps[i][j] == 'L':
                L.append([i, j])

    # start 에서 lever 까지 거리
    start_to_lever_distance = BFS(S, L, visited, N, M, maps)

    # lever 까지 가지 못하는 경우
    if start_to_lever_distance == -1:
        return -1
    else:
        # visited 초기화
        visited = [[0] * M for _ in range(N)]
        # lever 에서 end 까지 거리
        lever_to_end_distance = BFS(L, E, visited, N, M, maps)

    # start 에서 lever 까지는 갈 수 있지만, lever 에서 end 까지 가지 못하는 경우
    if lever_to_end_distance == -1:
        return -1
    else:
        return start_to_lever_distance + lever_to_end_distance

