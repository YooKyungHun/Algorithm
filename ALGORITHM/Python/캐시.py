from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.upper()

        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            # cache 가 꽉차있는 경우 맨 앞에서 하나빼고 넣어줘야 함
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5

    return answer