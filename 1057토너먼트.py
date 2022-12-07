N, A, B = map(int, input().split())

lst = []
for i in range(N):
    lst.append(i+1)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if A > B:
    A, B = B, A

flag = 1
cnt = 0

while flag:
    N = len(lst)

    # 홀수라면 마지막 원소를 pop 한 뒤에
    # 해당 토너먼트 끝나고 넣어주기
    if N % 2 == 1:
        last = lst.pop()

    for i in range(N//2):
        # while 문 종료조건
        # A 와 B 가 만나게 되는 경우
        # ex) A = 1, B = 2
        if lst[2*i] == A and lst[2*i+1] == B:
            flag = 0
            break

        # A 와 B 는 무조건 토너먼트에 올라가도록
        # 상대편을 0 으로 바꿔줌
        # ex) A = 2, B = 3, lst = [1, 2, 3, 4, 5, 6]
        # => lst = [0, 2, 3, 0, 5, 6]
        if lst[2*i] in (A, B):
            lst[2*i+1] = 0
        elif lst[2*i + 1] in (A, B):
            lst[2*i] = 0

        # A 와 B 가 무관한 대결의 경우
        # 큰 수가 토너먼트에 올라가도록
        # 작은 수를 0으로 바꿔줌(큰 수를 0 으로 바꿔도 상관 X)
        # ex) A = 2, B = 3, lst = [0, 2, 3, 0, 5, 6]
        # => lst = [0, 2, 3, 0, 0, 6]
        else:
            lst[2*i] = 0

    # 토너먼트에서 진 원소들(value == 0)
    # 제거하기
    # ex) A = 2, B = 3, lst = [0, 2, 3, 0, 0, 6]
    # => lst = [2, 3, 6]

    # remove() 메서드는 시간 복잡도가 O(N) / 시간초과 원인
    # while 0 in lst:
    #     lst.remove(0)
    remove_set = {0}
    lst = [i for i in lst if i not in remove_set]
    # lst = [i for i in lst if i != 0]

    if N % 2 == 1:
        lst.append(last)

    cnt += 1

print(cnt)