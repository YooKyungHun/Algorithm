from math import factorial


def solution(n, k):
    answer = []
    # cnt = 0
    # lst = [i+1 for i in range(n)]
    # for perm in permutations(lst, n):
    #     cnt += 1
    #     if cnt == k:
    #         return list(perm)

    lst = [i + 1 for i in range(n)]

    for i in range(n):
        tmp = (k - 1) // (factorial(n) / n)   # => (k - 1) % 2 + 1
        tmp = int(tmp)
        tmp = lst[tmp]

        answer.append(tmp)
        # print(answer)

        k -= lst.index(tmp) * (factorial(n) / n)
        lst.remove(tmp)
        n -= 1

    return answer

#     1 2 3
#     K      첫째자리수    K
#     1~2 => 1           K => (K-1) // 2 + 1
#     3~4 => 2
#     5~6 => 3

# --------------------------------------------------------------------

#     1 2 3 4
#     K     => 첫째자리수   K
#     1~6   => 1          K => (K-1) // 6 + 1
#     7~12  => 2
#     13~18 => 3
#     19~24 => 4

#     K                   => 둘째자리수
#     1~2, 15~16, 21~22   => 2
#     3~4, 9~10,  23~24   => 3
#     5~6, 11~12, 17~18   => 4
#     7~8, 13~14, 19~20   => 1

# [1, 2, 3, 4]
# [1, 2, 4, 3]
# [1, 3, 2, 4]
# [1, 3, 4, 2]
# [1, 4, 2, 3]
# [1, 4, 3, 2]
# [2, 1, 3, 4]
# [2, 1, 4, 3]
# [2, 3, 1, 4]
# [2, 3, 4, 1]
# [2, 4, 1, 3]
# [2, 4, 3, 1]
# [3, 1, 2, 4]
# [3, 1, 4, 2]
# [3, 2, 1, 4]
# [3, 2, 4, 1]
# [3, 4, 1, 2]
# [3, 4, 2, 1]
# [4, 1, 2, 3]
# [4, 1, 3, 2]
# [4, 2, 1, 3]
# [4, 2, 3, 1]
# [4, 3, 1, 2]
# [4, 3, 2, 1]

