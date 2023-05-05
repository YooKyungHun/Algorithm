'''
현재 누적되어 있는 데이터 중 가장 큰 값, 혹은 작은 값의 제거가 필요한 경우
사용할 수 있는 자료구조는 힙(heap) 자료구조이다.
파이썬의 heapq 는 최소힙 자료구조이기 때문에 최대힙을 사용하기 위해서는 음수처리하여 진행.

디펜스게임_s1 => heqpq 이용 => 통과
디펜스게임_s2 => list 이용 => 시간초과


(참고) https://yunaaaas.tistory.com/36
heapq - heapify: 주어진 리스트를 힙 정렬할 때 사용합니다. 이때의 Time Complexity는 O(n)입니다.
my_list = [3, 2, 1, 5, 7]
heapq.heapify(my_list) #[1,2,3,5,7]

heapq - heappop(heap): 가장 작은 원소를 빼낸 뒤, 나머지 원소가 힙을 유지하도록 정렬한다. O(logn)
my_list = [13, 2, 1, 5, 10]
heapq.heapify(my_list)
ret_val = heapq.heappop(my_list)
print("리턴된 값:", ret_val) # 1
print("남은 원소:", my_list) # [2,5,13,10]

heapq - heappush(heap, item):  리스트의 힙 상태를 유지하며, 데이터를 삽입시켜 줍니다. O(logn)
my_list = [13, 2, 1, 5, 10]
heapq.heapify(my_list)
heapq.heappush(my_list, 7) # 7 삽입
print("남은 원소:", my_list) # 남은 원소: [1, 2, 7, 5, 10, 13]

heapq - heap[0]: heap 리스트에서 가장 작은 원소를 삭제하지 않고 단순히 읽기만 합니다. O(1)
my_list = [13, 2, 1, 5, 10]
heapq.heapify(my_list)
print("리스트의 맨 앞 원소:", my_list[0]) # 리스트의 맨 앞 원소: 1
'''
from heapq import heappop, heappush

def solution(n, k, enemy):
    answer = 0
    heap = []

    for e in enemy:
        # 최대힙이므로 음수처리하여 저장
        heappush(heap, -e)
        # 일단 내가 가진 병사로 적군 처리
        n -= e

        # n 이 0 보다 작아진 경우
        if 0 > n:
            # 무조권이 없다면 게임 종료
            if k == 0:
                return answer

            # 무조권이 있다면
            else:
                # 최대힙에서 가장 많이 소모한 병사를 찾아서
                # 병사 다시 살려주기 (heappop(heap) 는 음수이므로 더해주는 개념임)
                n -= heappop(heap)
                k -= 1

        answer += 1
    return answer

# print(solution(2, 4, [3,3,3,3]))
# # # 4
# print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# # 5
# print(solution(7, 3, [5, 5, 5, 5, 2, 3, 1]))
# # ans : 5
# print(solution(1, 6, [2, 2, 2, 2, 3, 3, 1]))
# # # ans : 7
# print(solution(10, 1, [2, 2, 2, 2, 2, 10]))
# # # ans : 6
# print(solution(10, 1, [2, 2, 2, 2, 10]))
# # # ans : 5