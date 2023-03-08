from heapq import heappop, heappush, heapify


def solution(n, works):
    # Test Case 3번 과 같은 Edge Case 처리
    if sum(works) <= n:
        return 0

    # 파이썬은 최소힙만 지원해서, 최대힙으로 변경
    heap = [-work for work in works]
    heapify(heap)
    while n:
        # 1)
        # 가장 큰 값(- 가 붙은 것을 생각하면 가장 작은 값이기도 함)
        # heap[0] += 1
        # heapify(heap)
        # n -= 1

        # 2)
        mn = heappop(heap)
        heappush(heap, mn + 1)
        n -= 1
    if sum(heap) == 0:
        return 0
    else:
        return sum([i ** 2 for i in heap])
