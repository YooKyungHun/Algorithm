from collections import deque

def solution(s):
    answer = 0

    fst_count = 0
    other_count = 0

    for i in s:
        if fst_count == 0:
            # 첫번째 문자를 fst 에 저장
            fst = i

        # 그 다음부터 다음 문자와 fst 를 비교
        if i == fst:
            fst_count += 1
        else:
            other_count += 1

        if fst_count == other_count:
            # 정답 + 1, count 초기화
            answer += 1
            fst_count = 0
            other_count = 0


    # 진행하고 있다가 문자열이 끝난 경우
    if fst_count > 0:
        answer += 1

    return answer