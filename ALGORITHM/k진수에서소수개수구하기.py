from math import sqrt


def solution(n, k):
    def is_prime(n):
        for i in range(2, int(sqrt(n)) + 1):
            # 나누어 떨어지면 소수가 아님(False)
            if n % i == 0:
                return False
        return True

    k_jinsu_n = ''
    while n >= k:
        k_jinsu_n = str(n % k) + k_jinsu_n
        n = n // k
    k_jinsu_n = str(n) + k_jinsu_n
    # 	211020101011, str

    k_jinsu_n = '0' + k_jinsu_n + '0'
    # 02110201010110, str

    answer = []
    tmp = ''
    for i in range(1, len(k_jinsu_n)):
        # k_jinsu_n[i] != 0 일때
        if k_jinsu_n[i] != '0':
            tmp += k_jinsu_n[i]

        # k_jinsu_n[i] == 0 일때
        elif tmp != '':
            if int(tmp) == 1:
                tmp = ''

            elif is_prime(int(tmp)):
                answer.append(tmp)
                tmp = ''

    return len(answer)


'''
    1 2 4 5 10 20 25 50 100
    소수는 약수가 1과 자기 자신뿐인 수
    2가 약수면 50도 약수
    4가 약수면 25도 약수
    5가 약수면 20도 약수
    10이 약수면 10도 약수
    2부터 10까지 약수가 없다면 50부터 10까지 약수가 없는셈
    따라서 10까지만 확인해서 약수가 아니라면 10의 제곱은 소수
'''