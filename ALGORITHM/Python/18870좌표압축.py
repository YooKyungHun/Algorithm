N = int(input())
lst = list(map(int, input().split()))
lst_set = list(set(lst))
lst_set.sort()
# [-10, -9, 2, 4]

dic = {}
for i in range(len(lst_set)):
    dic[lst_set[i]] = i
# {-10: 0, -9: 1, 2: 2, 4: 3}

for i in range(len(lst)):
    print(dic[lst[i]], end=' ')

