from collections import deque

N, M, V = map(int, input().split())

arr = [[0] * (N+1) for _ in range(1+N)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
# v = [0, 1, 0, 0, 0]
# [[0, 0, 0, 0, 0],
#  [0, 0, 1, 1, 1],
#  [0, 1, 0, 0, 1],
#  [0, 1, 0, 0, 1],
#  [0, 1, 1, 1, 0]]

def DFS(V):
    # V = 현재 위치

    # i = 내가 갈 곳 탐색
    for i in range(1, N+1):
        if arr[V][i] == 1 and visited[i] == 0:
            visited[i] = 1
            print(i, end=' ')
            DFS(i)

print(V, end=' ')
visited[V] = 1
DFS(V)
print()


def BFS(V):
    queue = deque()
    queue.append(V)

    while queue:
        # 현재 위치
        V = queue.popleft()
        visited[V] = 1
        print(V, end=' ')

        # 내가 갈 곳 탐색
        for i in range(1, N+1):
            if arr[V][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)

visited = [0] * (N+1)
BFS(V)
