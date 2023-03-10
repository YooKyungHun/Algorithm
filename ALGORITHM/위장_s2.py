from collections import defaultdict, Counter
from itertools import combinations


def solution(clothes):
    dic = defaultdict(int)

    for cloth, type_cloth in clothes:
        dic[type_cloth] += 1
    # {'headgear': 2, 'eyewear': 1})

    tmp = []
    for i in dic.keys():
        tmp.append(dic[i])
    # [2, 1]

    N = len(dic)  # type_cloth 수

    # Edge Case: 모든 종류의 옷이 1벌씩 총 30벌 있는 경우
    tmp.sort()
    if tmp[-1] == 1:
        return 2 ** N - 1

    # N = 4
    # tmp = [1,2,3,4]
    전체조합수 = 0
    for i in range(1, N + 1):
        i종류에서의조합수 = 0
        for comb in combinations(tmp, i):

            각comb의곱 = 1
            for j in comb:
                각comb의곱 *= j

            i종류에서의조합수 += 각comb의곱
        전체조합수 += i종류에서의조합수
    return 전체조합수


'''
    # N = 4
    # tmp = [1,2,3,4]
comb
(1,) 1
(2,) 2
(3,) 3
(4,) 4
(1, 2) 2
(1, 3) 3
(1, 4) 4
(2, 3) 6
(2, 4) 8
(3, 4) 12
(1, 2, 3) 6
(1, 2, 4) 8
(1, 3, 4)
(2, 3, 4)
(1, 2, 3, 4)
'''