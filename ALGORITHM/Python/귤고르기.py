'''
func: list  사용 -> 시간초과
solution: hash 사용 -> 통과
'''

from collections import Counter

def func(k, tangerine):
    tangerine_set = list(set(tangerine))
    # 중복제거 [1,2,3,4,5]

    cnt = []
    for i in tangerine_set:
        cnt.append(tangerine.count(i))
        cnt.sort(reverse=True)
    cnt = deque(cnt)
    # 개수만 출력 [2,2,2,1,1]

    answer = 0
    while k > 0:
        k -= cnt[answer]
        answer += 1

    return answer

def solution(k, tangerine):
    # [1, 3, 2, 5, 4, 5, 2, 3]

    # count = Counter(tangerine)
    # {"1":1,"2":2,"3":2,"4":1,"5":2}

    # count = sorted(Counter(tangerine).values())
    # [1,1,2,2,2]

    # count = sorted(Counter(tangerine).items())
    # [[1,1],[2,2],[3,2],[4,1],[5,2]]

    count = Counter(tangerine).most_common()
    # [[3,2],[2,2],[5,2],[1,1],[4,1]]

    # count = sorted(Counter(tangerine).items(), reverse=True, key=lambda x: x[1])
    # [[3,2],[2,2],[5,2],[1,1],[4,1]]

    answer = 0
    for i, cnt in count:
        if k <= 0:
            break
        k -= cnt
        answer += 1

    return answer

# https://www.daleseo.com/python-collections-counter/

# collections.Counter() 메소드는 iterable 객체 즉, list, dict, set, str, bytes, tuple, range와 같은 반복 가능한 객체의 요소를 카운트하여 각각의 빈도 값을 {요소:빈도} 형태인 해쉬 테이블형태(카운터 객체)로 반환한다

# Counter 생성자는 여러 형태의 데이터를 인자로 받는데요. 먼저 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 됩니다.
# >>> Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
# Counter({'hi': 3, 'hey': 2, 'hello': 1})

# Counter 생성자에 문자열을 인자로 넘기면 각 문자가 문자열에서 몇 번씩 나타나는지를 알려주는 객체가 반환됩니다.
# >>> Counter("hello world")
# Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# collections 모듈의 Counter 클래스는 파이썬의 기본 자료구조인 사전(dictionary)를 확장하고 있기 때문에, 사전에서 제공하는 API를 그대로 다 시용할 수가 있습니다.
# 예를 들어, 대괄호를 이용하여 키로 값을 읽을 수 있고요.
# counter = Counter("hello world")
# >>> counter["o"], counter["l"]
# 2, 3

# most_common()
# 아마도 실전에서 Counter가 자주 쓰이는 경우는 가장 많이 나온 데이터나 가장 적게 나온 데이터를 찾을 때일 것일 텐데요.
# Counter 클래스는 이와 같은 작업을 좀 더 쉽게 할 수 있도록, 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 most_common()이라는 메서드를 제공하고 있습니다.
# >>> Counter('hello world').most_common()
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
# 이 메서드의 인자로 숫자 K를 넘기면 그 숫자 만큼만 리턴하기 때문에, 가장 개수가 많은 K개의 데이터를 얻을 수도 있습니다.
# Counter('hello world').most_common(2)
# [('l', 3), ('o', 2)]

# 산술 연산자 활용
# Counter가 재밌는 부분은 바로 마치 숫자처럼 산술 연산자를 사용할 수 있다는 것인데요.
# 예를 들어, 아래와 같이 2개의 카운터 객체가 있을 때,
# 이 두 객체를 더할 수도 있고요. 이 두 객체를 뺄 수도 있습니다.
# counter1 = Counter(["A", "A", "B"])
# counter2 = Counter(["A", "B", "B"])
# >>> counter1 + counter2
# Counter({'A': 3, 'B': 3})
# >>> counter1 - counter2
# Counter({'A': 1})