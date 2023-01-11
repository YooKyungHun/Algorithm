from collections import Counter


cnt = {"apple":2,"banana":3,"rice":2,"pork":2, "pot": 1}
cnt2= {"chicken":0,"apple":2,"banana":3,"rice":2,"pork":2, "pot": 1}
# cnt = {key: value for key, value in cnt.items() if value != 1}
# print(cnt)
#
# print(cnt.keys())
# print(cnt.items())
# print(cnt.values())

cnt = Counter(cnt)
cnt2 = Counter(cnt2)

print(cnt2-cnt == Counter())