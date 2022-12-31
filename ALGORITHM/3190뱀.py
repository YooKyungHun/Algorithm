from collections import deque

N = int(input())
K = int(input())
apple = []
for i in range(K):
    a, b = map(int, input().split())
    apple.append([a, b])
# [[3, 4], [2, 5], [5, 3]]

info = []
info_num = int(input())
for i in range(info_num):
    X, C = map(str, input().split())
    info.append([X, C])
# [['3', 'D'], ['15', 'L'], ['17', 'D']]

arr = [[0] * (N+2) for _ in range(N)]
arr.append([1]*(N+2))
arr.insert(0, [1]*(N+2))
for i in range(N+2):
    for j in range(N+2):
        if j == 0 or j == N+1:
            arr[i][j] = 1
for i in apple:
    a, b = i
    arr[a][b] = 2
arr[1][1] = 1
# 1 : 벽 or 뱀 자기 자신
# 2 : apple
# [[1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 0, 0, 0, 0, 0, 0, 1],
#  [1, 0, 0, 0, 0, 2, 0, 1],
#  [1, 0, 0, 0, 2, 0, 0, 1],
#  [1, 0, 0, 0, 0, 0, 0, 1],
#  [1, 0, 0, 2, 0, 0, 0, 1],
#  [1, 0, 0, 0, 0, 0, 0, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1]]

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 현재 뱀
queue = deque([])
queue.append((1, 1))



def turn(direction):
    global k
    if direction == 'D':
        k += 1  # 시계방향 회전
    else:
        k -= 1  # 반시계방향 회전

x, y = 1, 1
second = 0
k = 1
while True:
    second += 1
    x = x + dx[k % 4]
    y = y + dy[k % 4]

    # 벽에 부딪힌 경우 + 스스로 부딪힌 경우
    if arr[x][y] == 1:
        break

    # 사과를 먹은 경우
    elif arr[x][y] == 2:
        arr[x][y] = 1
        queue.append((x, y))

        # 방향전환
        if info and second == int(info[0][0]):
            direction = info.pop(0)[1]
            turn(direction)

    # 사과를 먹지 못한 경우
    elif arr[x][y] == 0:
        arr[x][y] = 1
        queue.append((x, y))
        rmx, rmy = queue.popleft()
        arr[rmx][rmy] = 0

        # 방향전환
        if info and second == int(info[0][0]):
            direction = info.pop(0)[1]
            turn(direction)

print(second)



