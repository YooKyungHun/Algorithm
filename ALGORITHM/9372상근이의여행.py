from collections import deque
import sys
input = sys.stdin.readline

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

    queue = deque()
    visited = [0] * (N+1)
    load = set()
    def BFS(a):
        visited[a] = 1
        queue.append(a)

        while queue:
            b = queue.popleft()

            if visited == [0] + ([1] * N):
                return len(load)

            for j in range(N+1):
                if arr[b][j] == 1 and visited[j] == 0:
                    queue.append(j)
                    load.add((b, j))
                    visited[j] = 1

    print(BFS(1))