def solution(word):
    # A 로 시작하는 단어의 수
    # A XXXX: (1563 - 1) / 2 = 781  (A~AUUUU)

    # 1글자(A     ) : 1개
    # 2글자(AX    ) : 5개
    # 3글자(AXX   ) : 25개
    # 4글자(AXXX  ) : 125개
    # 5글자(AXXXX ) : 625개

    # AE 로 시작하는 단어의 수 = (A로 시작하는 1글자 / 2글자 / 3글자 / 4글자 수의 합)
    # AE XXX: 1+5+25+125 = 156개

    arr = ['A', 'E', 'I', 'O', 'U']
    cnt = [781, 156, 31, 6, 1]
    answer = 0
    for i in range(len(word)):
        # word 의 각 글자가 arr 의 몇 번째 글자인지 찾음

        # 일반식: (781*N+1) + (156*N+1) + (31*N+1) + (5*N+1) + (1*N+1)
        # EIO()() 의 경우 (781*1+1) -> A 부터 E 직전까지 781개, E 1개
        # + (156*2+1) -> EA()()() 156 개, EE()()() 156 개, EI 1개
        # + (31*3+1)  -> EIA()() 31개, EIE 31개, EII 31개, EIO 1개
        #   = 1189
        answer += arr.index(word[i]) * cnt[i] + 1

    return answer