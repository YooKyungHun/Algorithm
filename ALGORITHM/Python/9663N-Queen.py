import copy
import sys
sys.setrecursionlimit(10**9)

N = int(input())

arrr = [[0] * N for _ in range(N)]
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

def func(tmp, n):
    for nx, ny in tmp:
        arr[nx][ny] = n

def DFS(queen):
    global cnt
    x, y = queen
    arr[x][y] = 2
    tmp = []

    for m in range(1, N):
        for k in range(8):
            nx, ny = x + (dx[k] * m), y + (dy[k] * m)
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                tmp.append([nx, ny])

    func(tmp, 1)
    for i in range(N):
        if x != N-1 and arr[x+1][i] == 0:
            DFS([x+1, i])

    if sum(map(sum, arr)) == N * N + N:
        cnt += 1

    func(tmp, 0)
    arr[x][y] = 0

cnt = 0
if N % 2 == 0:  # 짝수
    for i in range(N // 2):
        arr = copy.deepcopy(arrr)
        DFS([0, i])
    print(cnt * 2)

else:   # 홀수
    for i in range(N // 2):
        arr = copy.deepcopy(arrr)
        DFS([0, i])
    cnt = cnt * 2
    DFS([0, N//2])
    print(cnt)
