import sys
input = sys.stdin.readline

check = [True for _ in range(1000000 + 1)]
# i=sqrt(n)까지 검사
# 1000 이후의 수(2000, 3000, 4000, 5000, ...) 는
# 1000의 배수이기도 하지만
# 각각 2의 배수, 3의 배수, 4의 배수, 5의 배수이기 때문에
# 이미 check[j] = False 가 끝남.
for i in range(2, 1001):
    if check[i]:                                # i 가 소수인 경우
        for j in range(i + i, 1000000 + 1, i):  # i 이후 i의 배수들을 False 판정
            check[j] = False                    # 소수아님
lst = [i for i in range(3, 1000000 + 1) if check[i] is True]
# n = 20 일 때, lst = [3, 5, 7, 11, 13, 17, 19]

def Goldbach(n):
    global lst
    for i in lst:
        if check[n-i] is True:
        # if n-i in lst:
            return (f'{n} = {i} + {n-i}')
    return "Goldbach's conjecture is wrong."

while True:
    n = int(input())
    if n != 0:
        print(Goldbach(n))
    else:
        break

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