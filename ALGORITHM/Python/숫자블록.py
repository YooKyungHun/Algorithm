def solution(begin, end):
    N = end - begin + 1

    tmp = [1] * N

    # tmp[n] = n 의 약수 중 자기 자신을 제외한 1천만 이하의 최대약수

    # 16의 약수를 구하기 위해서는 n ** 1/2 까지 반복해서
    # def func(n):
    #     for i in range(1, n ** 1/2 + 1):
    #         if n // i == 0:
    #             i => 1 2 4 8 16 인데
    #             i 를 4 까지만 돌려도 알 수 있음
    #
    # 1 2 3 4 5 6 7 8 9 10 일 때, 10 ** 1/2 + 1 까지만 돌려도, 2 -> 5 로 예측가능
    # 0 1 1 2 1 3 1 4 3 5

    for i in range(begin, end + 1):
        if i == 1:
            tmp[0] = 0
            continue

        for j in range(2, int(i ** (1 / 2)) + 1):
            # j 가 i 의 약수라면(1을 제외하고 가장 작은 약수인 j 를 찾아서 곱셈 보수가 되는 i/j 를 찾기)
            if i % j == 0:
                tmp[i - begin] = j

                # ex) j 가 2 이면 -> tmp[i-begin] = i / 2
                if i / j <= 10_000_000:
                    tmp[i - begin] = i / j
                    break

    return tmp