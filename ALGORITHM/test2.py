from collections import Counter

cnt = Counter('hello world').most_common(2)

arr = [[3,2],[2,2],[5,2],[1,1],[4,1]]

for b,a in arr:
    print(b,a)

type = {"R":0,"T":3,"C":1,"F":0,"J":0,"M":2,"A":1,"N":1}
print(type[0])