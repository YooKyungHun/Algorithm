def solution(word):
    words = []

    def orderWords(input):
        AEIOU = 'AEIOU'

        if len(input) == 5:
            return

        for i in AEIOU:
            # input = input + i 를 사용하면
            # AAAA - AAAAA 이후 AAAAE 가 아니라 AAAAAE가 되어버림.
            words.append(input + i)
            orderWords(input + i)

    orderWords('')

    answer = words.index(word) + 1
    return answer

