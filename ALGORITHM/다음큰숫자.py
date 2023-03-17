def solution(n):
    answer = n+1
    check = bin(n).count('1')
    while True:
        if check == bin(answer).count('1'):
            break
        answer += 1
    return answer