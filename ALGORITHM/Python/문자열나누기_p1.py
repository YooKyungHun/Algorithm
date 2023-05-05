def solution(s):
    answer = 0

    while s:
        fst_char = s[0]

        if len(s) == 1:
            return answer + 1

        fst_char_cnt = 0
        other_char_cnt = 0

        flag = 1
        for i in s:
            if i == fst_char:
                fst_char_cnt += 1
            else:
                other_char_cnt += 1

            if fst_char_cnt == other_char_cnt:
                s = s[fst_char_cnt * 2:]
                answer += 1
                flag = 0
                break

        if flag:
            return answer + 1

    return answer