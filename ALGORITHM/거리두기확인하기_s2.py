from collections import deque


def isvalid(place):
    q = deque()

    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                q.append((i, j, i, j, 0))

    while q:
        x, y, start_x, start_y, distance = q.popleft()

        if distance < 2:
            for nx, ny in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
                if 0 <= nx < 5 and 0 <= ny < 5:
                    # 다시 출발점으로 되돌아가는 경우 방지
                    if (nx, ny) != (start_x, start_y):
                        if place[nx][ny] == 'P':
                            return 0
                        elif place[nx][ny] == 'O':
                            q.append((nx, ny, start_x, start_y, distance + 1))

    return 1

def solution(places):
    return [isvalid(place) for place in places]
