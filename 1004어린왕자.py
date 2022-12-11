TC = int(input())

def func(cx, cy, r):
    global cnt
    # 출발점과 도착점이 원 안에 있는 경우 count
    # (x-a)^2 + (y-b)^2 < r**2
    if (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2:
        cnt += 1
    if (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2:
        cnt += 1

    # 출발점과 도착점이 같은 원 안에 있을 경우 -2
    # ex) 돼지코 모양: 큰 원 안에 작은 원 2개가 있고,
    # 출발점과 도착점이 각각 작은 원 안에 있는 경우,
    # 큰 원의 개수 * 2 만큼 빼주기
    if (x1 - cx) ** 2 + (y1 - cy) ** 2 <= r ** 2 and (x2 - cx) ** 2 + (y2 - cy) ** 2 <= r ** 2:
        cnt -= 2
    return cnt

for tc in range(1, TC+1):
    # 출발점과 도착점
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input()) # 원의 개수
    cnt = 0

    for i in range(n):
        # 원의 모양
        cx, cy, r = map(int, input().split())
        func(cx, cy, r)
    print(cnt)























