from collections import deque


def solution(people, limit):
    answer = 0
    weight = 0
    prev = 0

    people.sort()
    queue = deque(people)

    while len(queue) >= 2:
        if queue[0] + queue[-1] <= limit:
            answer += 1
            queue.pop()
            queue.popleft()

        else:
            queue.pop()
            answer += 1

    if queue:
        answer += 1

    return answer

