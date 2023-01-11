from collections import Counter, defaultdict


def solution(want, number, discount):
    answer = 0
    want_dict = defaultdict(int)

    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    # 	{'banana': 3, 'apple': 2, 'rice': 2, 'pork': 2, 'pot': 1}
    want_dict = Counter(want_dict)

    disc_dict = defaultdict(int)
    for i in range(10):
        disc_dict[discount[i]] += 1
    #  {"chicken":1,"apple":3,"banana":2,"rice":2,"pork":2}
    disc_dict = Counter(disc_dict)

    for i in range(len(discount) - 10):
        # disc_dict == want_dict 로 표현하면
        # {"chicken": 0} 때문에 같지 않게 연산됨
        if disc_dict - want_dict == Counter():
            answer += 1

        disc_dict[discount[i]] -= 1
        disc_dict[discount[i + 10]] += 1

    if disc_dict - want_dict == Counter():
        answer += 1

    return answer