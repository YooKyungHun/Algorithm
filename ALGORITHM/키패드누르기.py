from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(thumb, number):
    global dx, dy
    queue = deque()
    queue.append(thumb)
    visited = [[0] * 3 for _ in range(4)]
    visited[thumb[0]][thumb[1]] = 1

    while queue:
        x, y = queue.popleft()
        if x == number[0] and y == number[1]:
            return visited[x][y]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < 4 and 0 <= ny < 3 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])


def solution(numbers, hand):
    answer = ''

    left_thumb = [3, 0]
    right_thumb = [3, 2]

    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*': [3, 0], 0: [3, 1], '#': [3, 2]}

    for number in numbers:
        if number in (1, 4, 7):
            left_thumb = dic[number]
            answer += 'L'

        elif number in (3, 6, 9):
            right_thumb = dic[number]
            answer += 'R'

        else:
            distance_with_left = BFS(left_thumb, dic[number])
            distance_with_right = BFS(right_thumb, dic[number])

            if distance_with_left < distance_with_right:
                left_thumb = dic[number]
                answer += 'L'
            elif distance_with_left > distance_with_right:
                right_thumb = dic[number]
                answer += 'R'
            elif distance_with_left == distance_with_right:
                if hand == 'left':
                    left_thumb = dic[number]
                    answer += 'L'
                else:
                    right_thumb = dic[number]
                    answer += 'R'

    return answer