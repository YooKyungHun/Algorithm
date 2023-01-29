from collections import Counter


def solution(X, Y):
    answer = ''
    cntX = Counter(X)
    cntY = Counter(Y)

    tmp = cntX & cntY  # 교집합
    # tmp = Counter({'0': 2}) / list(tmp) = ['0']
    # tmp = Counter({'1': 1, '0': 1}) / list(tmp) = ['1', '0']

    if list(tmp) == ['0']: return '0'
    if list(tmp) == []: return '-1'

    for i in range(9, -1, -1):
        i = str(i)
        answer += i * tmp[i]

    return answer