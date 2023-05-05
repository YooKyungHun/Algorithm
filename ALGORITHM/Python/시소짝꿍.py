from collections import Counter

def solution(weights):
    answer = 0

    people_cnter = Counter(weights)
    # Counter({100: 2, 180: 1, 360: 1, 270: 1})

    for weight, num_of_people in people_cnter.items():
        # 같은 몸무게를 가진 사람끼리 경우의 수 계산
        answer += num_of_people * (num_of_people - 1) / 2

        # 2배, 3/2배, 4/3배 몸무게를 가진 사람의 수를 구해서 계산
        answer += people_cnter[weight * 2] * num_of_people

        answer += people_cnter[weight * 3 / 2] * num_of_people

        answer += people_cnter[weight * 4 / 3] * num_of_people

    return answer