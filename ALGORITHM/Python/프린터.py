from collections import deque
from heapq import heapify, heappop, heappush


def solution(priorities, location):
    answer = 0

    # value 만을 이용한 최대 heap
    heap = [-value for value in priorities]
    heapify(heap)

    arr = [(idx, value) for idx, value in enumerate(priorities)]
    queue = deque(arr)
    # [(0, 2), (1, 1), (2, 3), (3, 2)]

    while True:
        idx, value = queue[0]

        # 가장 앞에 있는 문서(J) 보다 중요도가 더 높은 문서가 있다면
        if value < -heap[0]:
            # 맨 뒤로 넣기
            queue.rotate(-1)

        # 가장 앞에 있는 문서(J) 가 가장 중요한 문서라면
        elif value == -heap[0]:
            # 인쇄
            big_idx, big_value = queue.popleft()
            heappop(heap)

            # 몇 번째 인쇄인지
            answer += 1

            if big_idx == location:
                return answer

    return answer

# 2 1 3 2
# A B C D
# B C D A
# C D A B
# D A B   - C
# A B     - D
# B       - A
#         - B