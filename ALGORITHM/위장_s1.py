"""
하의 2개, 상의 3개가 있을 때
*잘못된 풀이
combinations으로 하의만 입을때, 상의만 입을때, 둘다 입을때 경우의 수를 구한다
*맞는 풀이
(하의 2개+안입은 경우) * (상의 3개 + 안입은 경우) = 3 * 4 = 12
그리고 전체에서 -1 (전부다 안입는 경우의 수를 뺀다)
즉 12 - 1 = 11
"""

from collections import defaultdict, Counter
from itertools import combinations

def solution(clothes):
    dic = defaultdict(int)

    for cloth, type_cloth in clothes:
        dic[type_cloth] += 1
    # {'headgear': 2, 'eyewear': 1})

    answer = 1
    for value in dic.values():
        answer *= (value+1)
    return answer - 1