def solution(n):
    ans = 0

    while n > 0:
        # 짝수
        if n % 2 == 0:
            n = n / 2

        # 홀수
        else:
            n = n - 1
            ans += 1

    #     5000
    #     2500
    #     1250
    #     625

    #     624
    #     312
    #     156
    #     78
    #     39

    #     38
    #     19

    #     18
    #     9

    #     8
    #     4
    #     2
    #     1

    #     0

    return ans