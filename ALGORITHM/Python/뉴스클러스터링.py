from collections import defaultdict, Counter


def solution(str1, str2):
    inter_dic = {}
    union_dic = {}

    # 대문자로 변경
    str1 = str1.upper()
    str2 = str2.upper()

    # 숫자, 특수문자, 공백 제거
    tmp = []
    for i in range(len(str1) - 1):
        if ('A' <= str1[i] <= 'Z' and 'A' <= str1[i + 1] <= 'Z'):
            tmp.append(str1[0 + i: 2 + i])
        else:
            continue
    cnt1 = Counter(tmp)

    tmp = []
    for i in range(len(str2) - 1):
        if ('A' <= str2[i] <= 'Z' and 'A' <= str2[i + 1] <= 'Z'):
            tmp.append(str2[0 + i: 2 + i])
        else:
            continue
    cnt2 = Counter(tmp)

    # Counter({'FR': 1, 'RA': 1, 'AN': 1, 'NC': 1, 'CE': 1})
    # Counter({'FR': 1, 'RE': 1, 'EN': 1, 'NC': 1, 'CH': 1})

    for i in cnt1:
        if i in cnt2:
            inter_dic[i] = min(cnt1[i], cnt2[i])
            union_dic[i] = max(cnt1[i], cnt2[i])
        else:
            union_dic[i] = cnt1[i]

    for i in cnt2:
        if i not in cnt1:
            union_dic[i] = cnt2[i]

    # print(inter_dic)
    # print(union_dic)

    sum_1, sum_2 = 0, 0
    for i in inter_dic.values():
        sum_1 += i
    for i in union_dic.values():
        sum_2 += i

    # print(sum_1, sum_2)
    if sum_1 + sum_2 == 0:
        return 65536

    return int((sum_1 / sum_2) * 65536)

    # A = Counter([1, 1, 2, 2, 3])
    # B = Counter([1, 2, 2, 4, 5])
    # print(A) Counter({1: 2, 2: 2, 3: 1})
    # print(B) Counter({2: 2, 1: 1, 4: 1, 5: 1})
    # print(A&B) Counter({2: 2, 1: 1})
    # print(A+B) Counter({2: 4, 1: 3, 3: 1, 4: 1, 5: 1})

    # A = Counter({1,1,2,2,3})
    # B = Counter({1,2,2,4,5})
    # print(A) // Counter({1: 1, 2: 1, 3: 1})
    # print(B) // Counter({1: 1, 2: 1, 4: 1, 5: 1})
    # # print(A&B)  // Counter({1: 1, 2: 1})
    # # print(A+B)  // Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1})
    # print(A&B) => 교집합 성립 X
    # print(A+B) => 합집합 성립 X