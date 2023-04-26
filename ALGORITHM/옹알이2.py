def check(word, flag):
    # "aya", "ye", "woo", "ma"
    nextflag = 0
    if word[0:2] == "ye":
        nextflag = 1
    elif word[0:2] == "ma":
        nextflag = 2
    elif word[0:3] == "aya":
        nextflag = 3
    elif word[0:3] == "woo":
        nextflag = 4
    else:
        return False

    # 전 flag 와 nextflag 가 같다면, 똑같은 문자열의 반복
    if flag == nextflag:
        return False

    # nextflag 에 따라 word 를 잘라주기
    if nextflag <= 2:
        word = word[2:]
    else:
        word = word[3:]

    # 다 성공적으로 잘랐다면
    if len(word) == 0:
        return True

    return check(word, nextflag)


def solution(words):
    answer = 0

    for word in words:
        flag = 0
        if check(word, flag):
            answer += 1

    return answer