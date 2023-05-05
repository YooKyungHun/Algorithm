from collections import deque

def solution(x, y, n):

    queue = deque()
    queue.append(x)
    visited = [0] * 1000001

    while queue:
        x = queue.popleft()
        if x == y:
            return visited[y]

        for nx in (2 * x, 3 * x, x + n):
            # 1000001 이 아니라 y 보다 클 이유가 없음
            if 0 <= nx <= y and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                queue.append(nx)

    return -1