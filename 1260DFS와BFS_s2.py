from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

DFS_result = []
# DFS_visited = [0] * (N+1)
DFS_visited = []
# DFS_visited[V] = 1
DFS_visited.append(V)

def DFS(V):
    if V not in DFS_result:
        DFS_result.append(V)
    if len(DFS_result) == N:
        return

    for i in range(N+1):
        if i in arr[V] and i not in DFS_visited:
            DFS_visited.append(i)
            DFS(i)
            DFS_visited.remove(i)


BFS_result = []
# BFS_visited = [0] * (N+1)
BFS_visited = []
# BFS_visited[V] = 1
BFS_visited.append(V)
def BFS(V):
    queue = deque()
    queue.append(V)
    if len(BFS_result) == N:
        return

    while queue:
        tmp = queue.popleft()
        if tmp not in BFS_result:
            BFS_result.append(tmp)

        for i in range(N+1):
            if i in arr[tmp] and i not in BFS_visited:
                BFS_visited.append(i)
                queue.append(i)

DFS(V)
BFS(V)
print(*DFS_result)
print(*BFS_result)