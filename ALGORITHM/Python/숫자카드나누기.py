'''
최대공약수 구할 때 gcd 를 쓰지 않고 for 문을 사용하면 시간소모가 너무 큼
따라서 GCD_A 를 구하는 방법을 지양하고
GCD_B 를 구하는 방법으로 사용할 것

python 3.9 이상에서 gcd(n1, n2, n3, n4, ...) 등 여러 인자를 받을 수 있음
만약 리스트를 같은 방식으로 이용하고자 한다면
gcd(*lst)
그러나 PRGM 가 python 3.85 임
'''
from math import gcd


def solution(arrayA, arrayB):
    answer = []

    # arrayA 의 최대공약수
    #     for i in range(min(arrayA), 0, -1):
    #         flag = 1
    #         for A in arrayA:
    #             if A % i != 0:
    #                 flag = 0
    #                 break

    #         if flag == 1:
    #             GCD_A = i
    #             break

    GCD_A = 0
    for i in range(len(arrayA)):
        GCD_A = gcd(GCD_A, arrayA[i])

    # arrayB 의 최대공약수
    GCD_B = 0
    for i in range(len(arrayB)):
        GCD_B = gcd(GCD_B, arrayB[i])

    # python 3.9 이상에서 gcd(n1, n2, n3, n4, ...) 등 여러 인자를 받을 수 있음
    # 만약 리스트를 같은 방식으로 이용하고자 한다면
    # gcd(*lst)
    # 그러나 PRGM 가 python 3.85

    # B 의 최대공약수가
    flag = 1
    for A in arrayA:
        # arrayA 의 원소 중 하나라도 나누어 떨어지면 안됨
        if A % GCD_B == 0:
            flag = 0
            break
    if flag == 1:
        answer.append(GCD_B)

    # A 의 최대공약수가
    flag = 1
    for B in arrayB:
        # arrayB 의 원소 중 하나라도 나누어 떨어지면 안됨
        if B % GCD_A == 0:
            flag = 0
            break
    if flag == 1:
        answer.append(GCD_A)

    return max(answer) if answer != [] else 0

#     array A              Group A
#     10, 17      의 공약수 1
#     10, 20      의 공약수 1, 2, 5, 10
#     14, 35, 119 의 공약수 1, 7
#     ㄱ, ㄴ, ㄷ

#     array B              Group B
#     5, 20       의 공약수 1, 5
#     5, 17       의 공약수 1
#     18, 30, 102 의 공약수 1, 2, 3, 6

# 최대공약수로 나누어 떨어지면, 최대공약수의 약수인 공약수로도 나누어 떨어짐

# 6 으로 ㄱ, ㄴ, ㄷ 중 하나라도 나누어 떨어지면, 그 수는 1, 2, 3 으로도 나누어 떨어짐. 따라서 조건 충족 양의 정수 없음.
# 6 으로 ㄱ, ㄴ, ㄷ 중 하나도 나누어 안 떨어지면, 1, 2, 3 으로 나누어 떨어질 수도 있고, 나누어 안 떨어질 수도 있지만,
# 가장 큰 양의 정수 6 이 확정됨.