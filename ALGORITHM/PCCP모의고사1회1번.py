from collections import deque, Counter

def solution(input_string):
    tmp = []

    # 거꾸로
    reversed_input_string = input_string[::-1]

    cnt = Counter(input_string)
    # Counter({'a': 3, 'e': 2, 'd': 2, 'b': 2, 'c': 2})

    for key in cnt.keys():
        if cnt[key] >= 2:
            key_first_index = input_string.index(key)
            key_last_index = input_string.rindex(key)
            # key_last_index = (len(input_string) - 1) - reversed_input_string.index(key)

            if key_first_index + cnt[key] - 1 < key_last_index:
                tmp.append(key)
            # 0   5
            # e ? e => e 는 4개 (cnt['e'] = 4)
            # => first_index 에 key 의 개수를 더했는데도(first_index 포함하므로 1 뺌)
            # => last_index 가 더 크다면 중간에 다른 문자가 껴있는 것

    if len(tmp) == 0:
        return "N"
    else:
        tmp.sort()
        return ''.join(tmp)