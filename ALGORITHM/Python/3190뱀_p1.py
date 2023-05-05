from collections import deque, defaultdict

N = int(input())
K = int(input())

apple = []
for i in range(K):
    a, b = map(int, input().split())
    apple.append([a, b])
# [[3, 4], [2, 5], [5, 3]]

L = int(input())

info = defaultdict(int)
for i in range(L):
    X, C = map(str, input().split())
    info[X] = C

# 방향전환
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
k = 0
def turn(direction):
    global k
    if direction == 'D':
        k += 1  # 시계방향 회전
    else:
        k -= 1  # 반시계방향 회전

# arr 지도(1: 벽, 2: 사과)
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


snake = deque()
snake.append([1, 1])
second = 0
now_x, now_y = 1, 1
while True:
    second += 1
    next_x = now_x + dx[k % 4]
    next_y = now_y + dy[k % 4]

    # 벽에 부딪힌 경우 + 스스로 부딪힌 경우
    if arr[next_x][next_y] == 1:
        break

    # 사과를 먹은 경우
    elif arr[next_x][next_y] == 2:
        arr[next_x][next_y] = 1
        snake.append((next_x, next_y))

    # 사과를 먹지 못한 경우
    elif arr[next_x][next_y] == 0:
        arr[next_x][next_y] = 1
        snake.append((next_x, next_y))
        remove_x, remove_y = snake.popleft()
        arr[remove_x][remove_y] = 0

    if info[str(second)]:
        turn(info[str(second)])

    now_x, now_y = next_x, next_y

print(second)
