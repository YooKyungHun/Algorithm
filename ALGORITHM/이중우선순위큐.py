from heapq import heappop, heappush, heapify, nlargest, nsmallest


def solution(operations):
    heap = []
    heapify(heap)

    for oper in operations:
        char, number = map(str, oper.split())

        # heap 원소 추가
        if char == 'I':
            heappush(heap, int(number))

        # 무시
        elif len(heap) == 0:
            continue

        # 최댓값 삭제
        elif char == 'D' and number == '1':
            heap.remove(nlargest(1, heap)[-1])

        # 최솟값 삭제
        elif char == 'D' and number == '-1':
            heappop(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        return [nlargest(1, heap)[-1], heap[0]]

# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])