'''
0) 높이나 너비의 차이가 한 칸일 경우, 접하지 않았어도 접한 것처럼 표현이 되기 때문에
기존의 크기보다 2배 계산하여 변수로 표현
1) 일반적인 BFS 문제로 풀되, isInRectangle 를 통해 다음 위치가 어떤 사각형의 내부에 있지 않도록,
isOutRectangle 를 통해 다음 위치가 모든 사각형의 외부에 있지 않도록 조건 설정

'''






from collections import deque

# 모든 사각형의 외부에 있어서는 안됨
def isOutRectangle(rectangle, nx, ny):
    flag = 0
    for leftX, leftY, rightX, rightY in rectangle:
        # 한 사각형의 외부에 있는 경우
        if nx < leftX or rightX < nx or ny < leftY or rightY < ny:
            flag += 1
    #         pass
    #     else:
    #         return False
    # return True

    # 모든 사각형의 외부에 있는 경우
    if flag == len(rectangle):
        return True
    else:
        return False


# 어떤 사각형(한개라도)의 내부에 있어서는 안됨
def isInRectangle(rectangle, nx, ny):
    for leftX, leftY, rightX, rightY in rectangle:
        if leftX < nx < rightX and leftY < ny < rightY:
            return True

    return False


def BFS(rectangle, characterX, characterY, itemX, itemY, visited, N):
    queue = deque()
    queue.append([characterX, characterY])
    visited[characterX][characterY] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        x, y = queue.popleft()

        if x == itemX and y == itemY:
            return visited[itemX][itemY] - 1

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            # 사각형 안에 있으면 안되기 때문에 isInRectangle 이 False 가 나와야 함
            # 모든 사각형 밖에 있다면 안되기 때문에 isOutRectangle 이 False 가 나와야 함
            if 0 <= nx < N and 0 <= ny < N and not isInRectangle(rectangle, nx, ny) and not isOutRectangle(rectangle,
                                                                                                           nx, ny) and \
                visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])


def solution(rectangle, characterX, characterY, itemX, itemY):
    N = max(map(max, rectangle))+1

    for i in range(len(rectangle)):
        for j in range(len(rectangle[i])):
            rectangle[i][j] *= 2

    characterX, characterY, itemX, itemY, N = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY, 2 * N

    visited = [[0] * (N + 1) for _ in range(N + 1)]

    answer = BFS(rectangle, characterX, characterY, itemX, itemY, visited, N)

    return answer // 2


print(solution([[1,1,5,7]], 1, 1, 4, 7))