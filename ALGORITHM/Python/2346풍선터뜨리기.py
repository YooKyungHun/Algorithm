from collections import deque

N = int(input())
lst = list(map(int, input().split()))

arr = [(i, v) for i, v in enumerate(lst, start=1)]
# [[0, 3], [1, 2], [2, 1], [3, -3], [4, -1]]
# [(0, 3), (1, 2), (2, 1), (3, -3), (4, -1)]

queue = deque(arr)

while queue:
    tmp, distance = queue.popleft()
    print(tmp, end=' ')

    if len(queue) == 0:
        break

    if distance > 0:
        distance = distance % len(queue)
        # for i in range(distance-1):
        # queue.rotate(-n): 왼쪽으로 n칸 밀어서 맨 오른쪽값을 왼쪽에 붙이기
        queue.rotate(-distance+1)

    else:
        distance = abs(distance) % len(queue)
        # for i in range(distance):
        # queue.rotate(n): 오른쪽으로 n칸 밀어서 맨 오른쪽값을 왼쪽에 붙이기
        queue.rotate(distance)

