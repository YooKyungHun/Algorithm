from collections import deque
import copy

dic = {']': '[', '}': '{', ')': '('}

def check(string):
    stack = []

    for i in string:
        # 열린 괄호
        if i in ('(', '{', '['):
            stack.append(i)

        # 닫힌 괄호
        else:
            # stack 이 비어있거나, 짝이 맞지 않다면
            if stack == [] or stack[-1] != dic[i]:
                return False
            # 짝이 맞는 경우: stack 의 열린 괄호 pop 하기
            stack.pop()

    # 스택에 남아있다면 (ex) input = "{{{{{"
    if stack:
        return False
    # for 문도 다 돌았고, stack 도 남아있지 않다면
    else:
        return True

def solution(string):
    answer = 0

    for i in range(len(string)):
        string_q = deque(string)
        string_q.rotate(-i)
        if check(string_q):
            answer += 1

    return answer


