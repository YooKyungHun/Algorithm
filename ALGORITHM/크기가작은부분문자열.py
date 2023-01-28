def solution(t, p):
    answer = 0

    for i in range(len(t) - len(p) + 1):
        number = int(t[0 + i:len(p) + i])
        if number <= int(p):
            answer += 1

    return answer