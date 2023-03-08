from heapq import heappop, heappush, heapify, nsmallest

def solution(n, works):
    if sum(works) <= n:
        return 0

    answer = 0
    days = len(works)
    tmp = [0] * days
    works = [-work for work in works]

    heapify(works)

    while works != tmp and n != 0:
        first_max = nsmallest(1, works)[-1]
        second_max = nsmallest(2, works)[-1]

        # [-1, -1] => gap = 1
        if first_max == second_max:
            gap = 1

        # [-6, -3, -3], n = 4 => gap = 3 => [-3, -3, -3], n = 1
        # [-9, -3, -3], n = 4 => gap = 4 => [-5, -3, -3], n = 0
        else:
            gap = min(abs(first_max - second_max), n)

        works[0] += gap
        n -= gap

        heapify(works)

    if works == [0] * days:
        return 0
    else:
        for work in works:
            answer += work ** 2
        return answer