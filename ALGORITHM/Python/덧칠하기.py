def solution(n, m, sections):
    answer = 0
    # o x x o o x x x x x
    # 1 2 3 4 5 6 7 8 9 10

    stack = []
    length = len(sections)
    idx = 0
    left = sections[idx]

    # while sections:
    #     if idx >= length:
    #         break
    for i in range(length):

        section = sections[i]

        if section - left > m - 1:
            answer += 1
            # print(section, "부터 ", left, "까지")

            # for j in range(m):
            #     if left + j in sections:
            #         sections.remove(left + j)

            left = section

    return answer + 1