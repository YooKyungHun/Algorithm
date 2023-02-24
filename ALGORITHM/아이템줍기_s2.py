'''
참고) https://school.programmers.co.kr/questions/32456
□ □ □ ■ ■ ■ ■ □ □ □ ㅣ □ □ □ ■ ■ ■ ■ □ □ □ㅣ □ □ □ ■ ■ ■ ■ □ □ □
□ □ □ ■ □ □ ■ □ □ □ ㅣ □ □ □ ■ ■ ■ ■ □ □ □ㅣ □ □ □ ■ □ □ ■ □ □ □
□ □ □ ■ □ □ ■ □ □ □ ㅣ □ □ □ ■ ■ ■ ■ □ □ □ㅣ □ □ □ ■ □ □ ■ □ □ □
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ㅣ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ㅣ ■ ■ ■ ■ □ □ ■ ■ ■ ■
■ □ □ ■ □ □ ■ □ □ ■ ㅣ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ㅣ ■ □ □ □ □ □ □ □ □ ■
■ □ □ ■ □ □ ■ □ □ ■ ㅣ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ㅣ ■ □ □ □ □ □ □ □ □ ■
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ㅣ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ㅣ ■ ■ ■ ■ □ □ ■ ■ ■ ■
□ □ □ ■ □ □ ■ □ □ □ ㅣ □ □ □ ■ ■ ■ ■ □ □ □ㅣ □ □ □ ■ □ □ ■ □ □ □
□ □ □ ■ □ □ ■ □ □ □ ㅣ □ □ □ ■ ■ ■ ■ □ □ □ㅣ □ □ □ ■ □ □ ■ □ □ □
□ □ □ ■ ■ ■ ■ □ □ □ ㅣ □ □ □ ■ ■ ■ ■ □ □ □ㅣ □ □ □ ■ ■ ■ ■ □ □ □

0) 높이나 너비의 차이가 한 칸일 경우, 접하지 않았어도 접한 것처럼 표현이 되기 때문에
기존의 크기보다 2배 계산하여 넓이가 4배가 되는 arr 에 표현
1) 주어진 좌표를 통해 도형을 그리는데, 내부가 꽉찬 직사각형을 그림
2) 주어진 좌표에서 상하좌우 한칸씩 줄여서 도형의 내부를 지워줌
'''


from collections import deque

def BFS(rectangle, characterX, characterY, itemX, itemY, edge, N, visited):
    characterX, characterY, itemX, itemY, N = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY, 2 * N
    queue = deque()
    queue.append([characterX, characterY])

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        x, y = queue.popleft()

        if x == itemX and y == itemY:
            return edge[itemX][itemY] - 1

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N + 1 and 0 <= ny < N + 1 and edge[nx][ny] != 0 and visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                edge[nx][ny] = edge[x][y] + 1

def solution(rectangle, characterX, characterY, itemX, itemY):
    N = max(map(max, rectangle))
    edge = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
    visited = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]

    for leftX, leftY, rightX, rightY in rectangle:
        leftX, leftY, rightX, rightY = 2 * leftX, 2 * leftY, 2 * rightX, 2 * rightY
        for i in range(leftX, rightX + 1):
            for j in range(leftY, rightY + 1):
                edge[i][j] = 1

    for leftX, leftY, rightX, rightY in rectangle:
        leftX, leftY, rightX, rightY = 2 * leftX, 2 * leftY, 2 * rightX, 2 * rightY
        for m in range(leftX + 1, rightX):
            for n in range(leftY + 1, rightY):
                edge[m][n] = 0

    # print(edge)

    # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    # [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    # [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    # [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    answer = BFS(rectangle, characterX, characterY, itemX, itemY, edge, N, visited)

    return answer // 2