def solution(n, words):
    prev = words[0][0]
    used_words = []

    for i in range(len(words)):
        now_word = words[i]

        if prev != now_word[0] or now_word in used_words:
            fail_person = i % n + 1
            fail_time = (i // n) + 1
            return [fail_person, fail_time]

        used_words.append(now_word)
        prev = now_word[-1]

    return [0, 0]
