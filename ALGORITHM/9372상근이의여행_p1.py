from collections import deque
import sys
input = sys.stdin.readline

TC = int(input())

def BFS(start):
    answer = 0
    queue = deque()
    queue.append(start)

    while queue:
        now = queue.popleft()

        if sum(visited) == N:
            return answer

        for next in range(1, N+1):
            if tree[now][next] == 1 and visited[next] == 0:
                visited[next] = 1
                queue.append(next)
                answer += 1


for tc in range(1, TC+1):
    N, M = map(int, input().split())

    tree = [[0] * (N+1) for _ in range(N+1)]
    visited = [0] * (N+1)

    for i in range(M):
        a, b = map(int, input().split())

        tree[a][b] = 1
        tree[b][a] = 1

    for start in range(1, N+1):
        if tree[1][start] == 1:
            visited[start] = 1
            print(BFS(start))
            break

    # [[0, 0, 0, 0],
    #  [0, 0, 1, 1],
    #  [0, 1, 0, 1],
    #  [0, 1, 1, 0]]



