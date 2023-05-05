from collections import deque

# now 와 word 를 비교해서 변환할 단어인지 판단하는 함수
def check(now, word):
    cnt = 0
    for i in range(len(word)):
        if now[i] != word[i]:
            cnt += 1
    if cnt == 1:
        return True
    return False


def solution(begin, target, words):
    N = len(words)
    visited = [0] * N

    visited.append(0)
    words.append(begin)

    queue = deque()
    queue.append(begin)

    while queue:
        now = queue.popleft()
        if now == target:
            return visited[words.index(target)]

        # 현재 now 에서
        # 변환할 word 를 탐색하는 반복문
        for word in words:
            if check(now, word) and visited[words.index(word)] == 0:
                queue.append(word)
                visited[words.index(word)] = visited[words.index(now)] + 1

    return 0