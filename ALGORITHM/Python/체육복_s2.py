def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)

    students = [1] * n
    for i in lost:
        students[i - 1] = 0
    for i in reserve:
        students[i - 1] = 2

    for i in range(0, n):
        if students[i] == 2:
            # 앞 번호 학생(i-1) 체크하고 뒷 번호 학생(i+1) 체크해야 에러가 안생김
            # 뒷 번호 학생 먼저 체크하면 반례생김
            # 1 2 3 4 5
            # 1 0 2 0 2
            # 2 0 2 0 1
            if i != 0 and students[i - 1] == 0:
                students[i] = students[i - 1] = 1
            elif i != n - 1 and students[i + 1] == 0:
                students[i] = students[i + 1] = 1

    answer = 0
    for student in students:
        if student >= 1:
            answer += 1
    print(students)
    return answer