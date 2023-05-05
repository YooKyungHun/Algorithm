N = int(input())
lst = list(map(int, input().split()))
students = int(input())
for i in range(students):
    gender, switch = map(int, input().split())
    switch = switch - 1
    # 남자
    if gender == 1:
        for j in range(switch, len(lst), switch+1):
            if lst[j] == 1:
                lst[j] = 0
            else:
                lst[j] = 1

    # [0, 1, 1, 1, 0, 1, 0, 1]
    # 여자
    if gender == 2:
        if lst[switch] == 1:
            lst[switch] = 0
        else:
            lst[switch] = 1

        flag = True
        count = 1
        while flag:
            if 0 <= switch - count and switch + count < len(lst) and lst[switch - count] == lst[switch + count]:
                # 둘 다 1이면 0으로 바꿔주고
                if lst[switch - count] == 1:
                    lst[switch - count] = 0
                    lst[switch + count] = 0

                # 둘 다 0이면 1으로 바꿔주고
                else:
                    lst[switch - count] = 1
                    lst[switch + count] = 1
                count += 1

            else:
                flag = False

if len(lst) > 20:
    while len(lst) > 20:
        print(*lst[0:20])
        lst = lst[20:]
    print(*lst)
else:
    print(*lst)