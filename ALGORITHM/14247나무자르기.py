N = int(input())
height = list(map(int, input().split()))
grow = list(map(int, input().split()))

trees = list((h, g) for h, g in zip(height, grow))
# [(1, 2), (3, 7), (2, 3), (4, 4), (6, 1)]

trees.sort(key=lambda x: x[1])
# [(6, 1), (1, 2), (2, 3), (4, 4), (3, 7)]


answer = 0
day = 1
for h, g in trees:
    answer += h + g * (day-1)
    day += 1

print(answer)

'''
g 2   7   3   4   1
h 1   3   2   4  '6'
 '3'  10  5   8   7
  5   17 '8'  12  8
  7   24  11 '16' 9
  9  '31' 14  20  0
  
  31 을 제일 나중에 베게 되는데 그 이유는 h 의 숫자가 커서가 아니라
  g 가 크기 때문에 가장 나중에 베는게 유리하기 때문.
  문제에서 여러 번 벨 수 있다고 했지만, 여러번 베면 효율이 떨어짐.
  즉, 고르게 되는 순서는 h 와는 관련없이 g 가 작은 것부터 베는 것이고,
  g 가 큰 것은 나중에 베는 것이 유리함.
  
  sort vs sorted vs lambda
  https://velog.io/@aonee/Python-%EC%A0%95%EB%A0%AC-sort-sorted-reverse
'''