def solution(phone_book):
    answer = True

    phone_book.sort(key=lambda x: -len(x))

    ph = set()

    for i in phone_book:

        # 만약 이미 있다면 False
        if i in ph:
            return False

        # 없다면, i 를 1글자, 2글자, 3글자... 로 잘라서 ph 에 add
        for j in range(1, len(i) + 1):
            ph.add(i[:j])
    return True