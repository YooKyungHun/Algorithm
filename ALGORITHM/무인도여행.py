import sys

sys.setrecursionlimit(10 ** 9)


def solution(maps):
    answer = []

    N, M = len(maps), len(maps[0])

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    def DFS(x, y):
        nonlocal food

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and maps[nx][ny] != "X":
                visited[nx][ny] = 1
                food += int(maps[nx][ny])
                DFS(nx, ny)

        return food

    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and maps[i][j] != 'X':
                visited[i][j] = 1
                food = int(maps[i][j])
                tmp = DFS(i, j)
                answer.append(tmp)

    if answer == []:
        return [-1]
    return sorted(answer)