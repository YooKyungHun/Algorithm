from collections import Counter

def solution(participant, completion):

    part_cnt = Counter(participant)
    comp_cnt = Counter(completion)

    answer = part_cnt - comp_cnt
    answer = list(answer)
    return answer[0]