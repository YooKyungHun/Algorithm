from collections import deque, Counter


def solution(s):
    answer = True

    # TC4 처럼 '(' 와 ')' 의 갯수가 서로 다른 경우
    cnt = Counter(s)
    if cnt['('] != cnt[')']:
        return False

    # TC4 제외하고 올바르지 못한 괄호
    queue = deque()
    for i in s:
        # ( 는 무조건 넣어줌
        if i == '(':
            queue.append(i)

        # ) 는 queue 가 비었는지와 queue 의 마지막 원소를 확인
        else:
            # TC 3
            if not queue:
                return False

            # TC 1
            if queue[-1] == '(':
                queue.pop()

    if queue:
        return False

    return True