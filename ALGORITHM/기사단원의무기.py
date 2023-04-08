def solution(number, limit, power):
    약수 = []
    for i in range(1, number + 1):
        cnt = 0

        for j in range(1, int(i ** 0.5) + 1):
            # 제곱근 이하의 약수에 대해 +2
            if i % j == 0:
                cnt += 2

            # 제곱근이면 -1
            if j ** 2 == i:
                cnt -= 1
        약수.append(cnt)
    # [1, 2, 2, 3, 2, 4, 2, 4, 3, 4]

    for i in range(len(약수)):
        if 약수[i] > limit:
            약수[i] = power

    return sum(약수)