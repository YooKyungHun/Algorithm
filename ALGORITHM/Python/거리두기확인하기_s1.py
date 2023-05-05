from itertools import combinations


def solution(places):
    answer = []

    def calc_distance(A, B, place):
        A_x, A_y = A[0], A[1]
        B_x, B_y = B[0], B[1]

        # 맨해튼 거리가 3이상이면 어차피 못가니까 통과
        if abs(A_x - B_x) + abs(A_y - B_y) >= 3:
            return True

            # 맨해튼 거리가 2이면, 한 줄에 있는지 or ㄱ 자 모양으로 있는지 확인
        if abs(A_x - B_x) + abs(A_y - B_y) == 2:
            # 두 사람이 가로 같은 줄에 있다면, 두 사람 사이의 공간이 파티션 여부 확인
            if A_x == B_x:
                if place[A_x][min(A_y, B_y) + 1] == "X":
                    return True
                else:
                    return False
            # 두 사람이 세로 같은 줄에 있다면, 두 사람 사이의 공간이 파티션 여부 확인
            elif A_y == B_y:
                if place[min(A_x, B_x) + 1][A_y] == "X":
                    return True
                else:
                    return False

            # 두 사람이 위치한 2*2 사각형에 파티션이 두 개 있어야만 통과
            else:
                cnt = 0
                for i in range(min(A_x, B_x), min(A_x, B_x) + 2):
                    for j in range(min(A_y, B_y), min(A_y, B_y) + 2):
                        if place[i][j] == "X":
                            cnt += 1
                if cnt == 2:
                    return True
                else:
                    return False

        # 맨해튼 거리가 1이면 붙어있으니까 거리두기 실패
        if abs(A_x - B_x) + abs(A_y - B_y) == 1:
            return False

    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))

        # print(people)
        # people = [(0, 0), (0, 4), (2, 1), (2, 3), (4, 0), (4, 4)]

        flag = True
        for A, B in combinations(people, 2):
            # print(A, B)
            if calc_distance(A, B, place) is False:
                answer.append(0)
                flag = False
                break

        if flag:
            answer.append(1)

    return answer


'''
[["POOOP", 
  "OXXOX", 
  "OPXPX", 
  "OOXOX", 
  "POXXP"], 

 ["POOPX", 
  "OXPXP", 
  "PXXXO", 
  "OXXXO", 
  "OOOPP"], 

 ["PXOPX", 
  "OXOXP",
  "OXPOX", 
  "OXXOP", 
  "PXPOX"], 

 ["OOOXX", 
  "XOOOX", 
  "OOOXX", 
  "OXOOX", 
  "OOOOO"], 

 ["PXPXP", 
  "XPXPX", 
  "PXPXP", 
  "XPXPX", 
  "PXPXP"]]
'''