from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1
    arr[b][a] = 1

    # [[0, 0, 0, 0, 0],
    #  [0, 0, 1, 1, 1],
    #  [0, 1, 0, 0, 1],
    #  [0, 1, 0, 0, 1],
    #  [0, 1, 1, 1, 0]]

ans = []
DFS_visited = [0] * (N+1)
def DFS(V):
    DFS_visited[V] = 1
    ans.append(V)

    # 현재위치 V 에서 다음에 가려는 i 찾기
    for i in range(N+1):
        if arr[V][i] == 1 and DFS_visited[i] == 0:
            DFS(i)


ans2 = []
BFS_visited = [0] * (N+1)
def BFS(V):
    BFS_visited[V] = 1
    queue = deque()
    queue.append(V)

    while queue:
        tmp = queue.popleft()
        ans2.append(tmp)

        # 현재위치 V 에서 다음에 가려는 i 찾기
        for i in range(N+1):
            if arr[tmp][i] == 1 and BFS_visited[i] == 0:
                BFS_visited[i] = 1
                queue.append(i)

DFS(V)
BFS(V)
print(*ans)
print(*ans2)

