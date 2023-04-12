from heapq import heappop, heappush, heapify, nlargest, nsmallest


def solution(operations):
    max_heap = []
    min_heap = []

    heapify(max_heap)
    heapify(min_heap)

    # tmp = [5, 4, 3, 2, 1]
    # heapify(tmp)
    # tmp.remove(5)
    # print(tmp)

    for operation in operations:
        oper, number = map(str, operation.split())
        number = int(number)

        if oper == "I":
            heappush(min_heap, number)
            heappush(max_heap, -number)

        elif oper == "D" and len(min_heap) == 0:
            continue


        # 최솟값 삭제
        elif oper == "D" and number == -1:
            tmp = heappop(min_heap)
            max_heap.remove(-tmp)
            heapify(max_heap)

        # 최댓값 삭제
        elif oper == "D" and number == 1:
            tmp = heappop(max_heap)
            min_heap.remove(-tmp)
            heapify(min_heap)

    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [-heappop(max_heap), heappop(min_heap)]

# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])