from collections import Counter

def solution(X, Y):
    answer = ''

    X, Y = Counter(X), Counter(Y)
    # Counter({'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '0': 1})
    # Counter({'0': 2, '1': 1})

    # {"0":1,"1":1,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}

    for i in range(9, -1, -1):
        i = str(i)
        K = min(X[i], Y[i])

        if i == '0' and answer == '' and K == 0:
            return str(-1)
        elif i == '0' and answer == '' and K != 0:
            return str(0)

        # 교집합의 개수(K) 만큼 반복(뒤에 붙여주기)
        answer = answer + i * K

    return answer