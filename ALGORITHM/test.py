from collections import Counter
from itertools import combinations


cnt = Counter({1: 4, 8: 2})

for i in cnt:
    print(i)
    print(cnt[i])

print('a' + 'b')
print('aab'[0:len('aab')-1])