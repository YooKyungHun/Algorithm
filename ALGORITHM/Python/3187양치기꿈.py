import sys
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())

arr = [list(map(str, input())) for _ in range(R)]
# [['.', '.', '.', '#', '.', '.'],
#  ['.', '#', '#', 'v', '#', '.'],
#  ['#', 'v', '.', '#', '.', '#'],
#  ['#', '.', 'k', '#', '.', '#'],
#  ['.', '#', '#', '#', '.', '#'],
#  ['.', '.', '.', '#', '#', '#']]

visited = [[0] * C for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def DFS(i, j):
    global k_cnt, v_cnt

    if arr[i][j] == 'k': k_cnt += 1
    if arr[i][j] == 'v': v_cnt += 1

    for k in range(4):
        ni, nj = i + dx[k], j + dy[k]

        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] in ('k', 'v', '.') and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            DFS(ni, nj)


# 살아남은 양과 늑대의 수
k_answer, v_answer = 0, 0
for i in range(R):
    for j in range(C):
        if arr[i][j] in ('k', 'v') and visited[i][j] == 0:
            # 한 구역 안에 있는 양과 늑대의 수
            k_cnt, v_cnt = 0, 0
            visited[i][j] = 1
            DFS(i, j)

            # 양 <= 늑대: 양 다 잡아먹힘
            if k_cnt <= v_cnt:
                k_cnt = 0
            # 양 > 늑대: 늑대 다 잡아먹힘
            else:
                v_cnt = 0

            k_answer += k_cnt
            v_answer += v_cnt

print(k_answer, v_answer)