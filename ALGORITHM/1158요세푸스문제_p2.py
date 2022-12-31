from collections import deque

N, K = map(int, input().split())
lst = [i+1 for i in range(N)]
# [1, 2, 3, 4, 5, 6, 7]

queue = deque(lst)

print('<', end='')
while len(queue) > 1:
    queue.rotate(-K+1)
    print(queue.popleft(), end=', ')
print(*queue, end='>')

