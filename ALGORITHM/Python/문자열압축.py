'''
print([1, 2, 3, 4][0: 10]) => [1, 2, 3, 4]
print([1, 2, 3, 4][2: 20]) => [3, 4]
print('abcabcdede'[9:12]) => 'abc' / 'abc' / 'ded' / 'e' => 'e'
'''

def solution(s):
    result = []

    # 몇 단위로 자를 건지
    for i in range(1, len(s) // 2 + 1):
        # 기준 문자열
        tmp = s[0:i]
        answer = ''
        cnt = 1

        # 잘리는 문자열의 시작점, 끝점
        # 끝부분 처리는 len(s) 보다 길게 처리(주석참고)
        for j in range(i, len(s) + i, i):
            # tmp 가 현재 문자열, s[j:j+i] 가 다음 문자열
            if tmp == s[j:j + i]:
                cnt += 1

            else:
                if cnt == 1:
                    answer += tmp
                    tmp = s[j:j + i]

                else:
                    answer += str(cnt) + tmp
                    # 기준 문자열에 다음 문자열 선정(초기화)
                    tmp = s[j:j + i]
                    cnt = 1

        result.append(len(answer))

    # TC 6 => s = 'a', output = 1
    return min(result) if len(s) != 1 else 1