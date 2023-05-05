from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
tmp = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(comb):
    # virus_q 랑 arr 를 항상(매 조합마다) 최신화 해주어야 함
    virus_q = deque(virus)
    arr = copy.deepcopy(tmp)

    for i in range(3):
        a, b = comb[i]
        arr[a][b] = 1

    while virus_q:
        x, y = virus_q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                arr[nx][ny] = 2
                virus_q.append([nx, ny])
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
    lst.append(cnt)

blank, virus = [], []
# 빈칸(0) 좌표가 들어있는 blank 리스트 만들기
# virus(2) 좌표가 들어있는 virus 리스트 만들기
for i in range(N):
    for j in range(M):
        if tmp[i][j] == 0:
            blank.append([i, j])
        if tmp[i][j] == 2:
            virus.append([i, j])

# 각 조합마다 안전영역의 넓이가 들어갈 리스트
lst = []

# blank 리스트를 이용해 빈 칸 세 개씩 조합만들기
for comb in combinations(blank, 3):
    BFS(comb)
    # BFS([[0, 4], [1, 3], [3, 3]])
print(max(lst))

