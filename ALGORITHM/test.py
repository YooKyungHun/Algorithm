def solution(cards1, cards2, goal):
    answer = ''
    flag = 0

    for i in cards2:
        for idx, value in enumerate(goal):
            if i == value:
                if idx >= flag:
                    flag = idx
                    continue
                else:
                    # print(i, j, k)
                    return 'No'
    flag = 0
    for i in cards1:
        for idx, value in enumerate(goal):
            if i == value:
                if idx >= flag:
                    flag = idx
                    continue
                else:
                    # print(i, j, k)
                    return 'No'

    return "Yes"

solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])