from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

blank, virus = [], []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            blank.append((i, j))
        if arr[i][j] == 2:
            virus.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0 ,1]

def BFS(arr_copy):
    queue = deque(virus)
    visited = [[0] * M for _ in range(N)]

    for x, y in queue:
        visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < M and arr_copy[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                arr_copy[nx][ny] = 2
                queue.append((nx, ny))

    safety_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr_copy[i][j] == 0:
                safety_cnt += 1

    return safety_cnt


answer = 0
for comb in combinations(blank, 3):
    arr_copy = copy.deepcopy(arr)
    for i in comb:
        a, b = i[0], i[1]
        arr_copy[a][b] = 1
    safety_cnt = BFS(arr_copy)
    answer = max(answer, safety_cnt)

print(answer)
