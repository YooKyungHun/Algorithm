check = [True for _ in range(1000000 + 1)]
# i=sqrt(n)까지 검사
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

