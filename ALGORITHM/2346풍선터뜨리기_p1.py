from collections import deque

N = int(input())

tmp = list(map(int, input().split()))
lst = deque()
for i, v in enumerate(tmp, 1):
    lst.append([i, v])
# [[1, 3], [2, 2], [3, 1], [4, -3], [5, -1]]

answer = []
while lst:
    a, b = lst[0]

    lst.popleft()
    answer.append(a)

    if not lst: break

    if b > 0:
        b = abs(b) % len(lst)
        lst.rotate(-(b-1))
    else:
        b = abs(b) % len(lst)
        lst.rotate(b)

print(*answer)