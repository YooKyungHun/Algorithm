from collections import deque

N = int(input())
L = int(input())

arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(L):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

def BFS():
    queue = deque()
    queue.append(1)
    visited[1] = 1

    while queue:
        now = queue.popleft()

        for i in range(1, N+1):
            if arr[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)

BFS()

print(sum(visited)-1)