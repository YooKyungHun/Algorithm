def solution(survey, choices):
    dic = {1: [0, 3], 2: [0, 2], 3: [0, 1], 4: [0, 0],
           5: [1, 1], 6: [1, 2], 7: [1, 3]}

    type = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
            'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i in range(len(choices)):
        who, point = dic[choices[i]]
        # (1 1) (0 1) (0 2) (1 3) (1 1)

        type[survey[i][who]] += point
    # type = {"R":0,"T":3,"C":1,"F":0,"J":0,"M":2,"A":1,"N":1}

    lst = [i for i in type.keys()]
    # lst = ["R","T","C","F","J","M","A","N"]

    answer = ''
    for i in range(4):
        if type[lst[2 * i]] >= type[lst[2 * i + 1]]:
            answer += lst[2 * i]
        else:
            answer += lst[2 * i + 1]

    # if type['R'] >= type['T']:
    #     answer += 'R'
    # else:
    #     answer += 'T'
    # if type['C'] >= type['F']:
    #     answer += 'C'
    # else:
    #     answer += 'F'
    # if type['J'] >= type['M']:
    #     answer += 'J'
    # else:
    #     answer += 'M'
    # if type['A'] >= type['N']:
    #     answer += 'A'
    # else:
    #     answer += 'N'

    return answer