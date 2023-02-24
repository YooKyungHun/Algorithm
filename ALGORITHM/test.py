from collections import deque


# def BFS(rectangle, characterX, characterY, itemX, itemY, visited):
#     queue = deque()
#     queue.append([characterX, characterY])
#     visited[characterX][characterY] = 1

#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]

#     while queue:
#         x, y = queue.popleft()

#         if x == itemX and y == itemY:
#             return visited[itemX][itemY] -1

#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]

#             # 사각형 안에 있으면 안되기 때문에 isInRectangle 이 False 가 나와야 함
#             # 모든 사각형 밖에 있다면 안되기 때문에 isOutRectangle 이 False 가 나와야 함
#             if not isInRectangle(rectangle, nx, ny) and not isOutRectangle(rectangle, nx, ny) and visited[nx][ny] == 0:
#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append([nx, ny])

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = max(map(max, rectangle))
    edge = [[0] * (N + 1) for _ in range(N + 1)]

    for leftX, leftY, rightX, rightY in rectangle:
        for i in range(leftX, rightX + 1):
            for j in range(leftY, rightY + 1):
                edge[i][j] == 1
    print(edge)
    #         for m in range(leftX + 1, rightX):
    #             for n in range(leftY + 1, rightY):
    #                 edge[m][n] == 0

    # print(edge)

    # answer = BFS(rectangle, characterX, characterY, itemX, itemY, visited)

    answer = 0
    return answer

solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)