from itertools import combinations
from collections import defaultdict, Counter


def solution(orders, course):
    answer = []
    for i in course:
        lst = []
        for order in orders:
            if i <= len(order):
                for comb in combinations(order, i):
                    tmp = ''.join(sorted(comb))
                    lst.append(tmp)
                    # ["XY","XZ","YZ","WX","XY","WY","WX","AW","AX"]

        cnt = Counter(lst)
        # Counter({'XY': 2, 'WX': 2, 'XZ': 1, 'YZ': 1, 'WY': 1, 'AW': 1, 'AX': 1})

        cnt_most = cnt.most_common()
        # [('XY', 2), ('WX', 2), ('XZ', 1), ('YZ', 1), ('WY', 1), ('AW', 1), ('AX', 1)] # list

        if cnt_most:  # 해당 조건 없으면, TC 3번에서 i = 4, max(len(order)) = 3 일때, lst 가 비어있기 때문에 에러발생
            most_count = cnt_most[0][1]  # 2

            for alphabet, counts in cnt_most:
                if most_count >= 2 and counts == most_count:
                    answer.append(alphabet)

    return sorted(answer)

