from string import ascii_lowercase


def solution(string, skips, index):
    answer = ''

    a_to_z = set(ascii_lowercase)
    a_to_z = a_to_z - set(skips)
    a_to_z = list(sorted(a_to_z))
    # ['a', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    N = len(a_to_z)

    for s in string:
        idx = a_to_z.index(s) + index
        idx = idx % N
        answer += a_to_z[idx]

    return answer