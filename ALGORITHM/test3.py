from collections import deque
from heapq import heapify, heappush, heappop
from math import gcd

# heap = [[1, 10], [1, 2], [2, 1], [1, 3], [1, -10], [1, 0], [1, 4], [1, 6], [1, 1]]
# heapify(heap)
#
# while heap:
#     print(heappop(heap))
#
# h = [[1, 1, 1], [1, 1, 3], [1, 2, 3],   [1, 1, 0], [1, 2, 0], [1, 1, 2],  [1, 2, 1],[1, 2, 2]]
# heapify(h)
#
# while h:
#     print(heappop(h))

lst = [5, 10, 15, 20]
print(gcd(5, 10, 15, 20))
print(gcd(*lst))