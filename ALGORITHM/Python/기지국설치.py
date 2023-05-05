def solution(n, stations, w):
    answer = 0

    #     4 11
    #     (1~2) 3 4 5 (6~9) 10 11
    #     2 / 4 -> 1 / 2

    #     9
    #     (1~6) 7 8 9 10 11 (12~16)
    #     6 / 5 -> 2 / 1

    # 일반적으로 stations 의 크기가 M 이라면,
    # 맨 앞과 맨 뒤를 포함하여, station 간의 사이의 개수는 M + 1

    tmp = []

    # 각 station 의 앞에 몇 개의 아파트가 전파도달이 안되는지 파악
    # 4, 11 이면 1~4중에 2 개, 4~11에 4 개
    for i in range(0, len(stations)):
        station = stations[i]

        if i == 0 and station - w - 1 > 0:
            tmp.append(station - w - 1)

        elif station - stations[i - 1] - 1 - 2 * w > 0:
            tmp.append(station - stations[i - 1] - 1 - 2 * w)  # 11 - 4 - 1 - 2 * w

    # 마지막 station 의 뒤에 몇 개의 아파트가 전파도달이 안되는지 파악
    # 11 뒤에 아파트 0 개, 9 뒤에 아파트 5 개
    if n - stations[-1] - w > 0:  # 16 - 9 - 2
        tmp.append(n - stations[-1] - w)

    # tmp = [2, 4] # tmp = [6, 5]

    for i in tmp:
        if i % (w * 2 + 1) == 0:
            answer += i // (w * 2 + 1)
        else:
            answer += i // (w * 2 + 1) + 1

    return answer