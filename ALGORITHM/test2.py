from collections import Counter
from itertools import combinations
from collections import deque
import copy


def solution(s):
    answer = 0

    for j in s:
        fst = j
        fst_count = 1
        other_count = 0

        for i in range(1, len(s)):
            if fst == s[i]:
                fst_count += 1
            else:
                other_count += 1

            if fst_count == other_count:
                s = s[fst_count * 2:]
                answer += 1
                break

        if i == len(s) - 1 or len(s) == 1:
            answer += 1
            break

    return answer


print(solution("aabbcddd"))