from collections import Counter

def solution(k, tangerine):

    count = Counter(tangerine).most_common()

    answer = 0
    for size, cnt in count:
        k -= cnt
        answer += 1
        if k <= 0:
            return answer
