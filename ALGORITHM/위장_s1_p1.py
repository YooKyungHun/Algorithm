from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)

    for cloth, type_cloth in clothes:
        dic[type_cloth] += 1

    answer = 1
    for value in dic.values():
        answer = answer * (value + 1)
    return answer - 1