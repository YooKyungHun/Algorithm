from collections import defaultdict
TC = int(input())

for tc in range(1, TC+1):
    n = int(input())
    cloth = defaultdict(list)

    for i in range(n):
        a, b = map(str, input().split())
        cloth[b].append(a)
    # {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']})

    tmp = 1
    # 둘 다 가능
    # for i in cloth.keys():
    for i in cloth:
            tmp *= (len(cloth[i])+1)

    print(tmp - 1)