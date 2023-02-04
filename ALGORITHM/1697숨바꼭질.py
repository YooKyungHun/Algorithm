from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001

# 5 17
# 5 - 10 - 9 - 18 - 17
#
# 5 17
# 5 - 4 - 8 - 16 - 17

def BFS(N, K):
    if N >= K:
        return N - K

    queue = deque()
    queue.append(N)
    visited[N] = 0

    while queue:
        # x = 현재위치
        x = queue.popleft()

        if x == K:
            return visited[K]

        # nx = 현재위치에서 갈 곳 탐색
        # nx = x + 1, x - 1, 2 * x
        for nx in (x + 1, x - 1, 2 * x):
            if 0 <= nx <= 100000 and visited[nx] == 0:
                queue.append(nx)
                visited[nx] = visited[x] + 1

print(BFS(N, K))