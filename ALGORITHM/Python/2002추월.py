import sys
input = sys.stdin.readline

N = int(input())
in_dict = {}
for i in range(N):
    in_dict[input()] = i
# {'ZG431SN': 0, 'ZG5080K': 1, 'ST123D': 2, 'ZG206A': 3}
out = list(input() for _ in range(N))
# ['ZG206A', 'ZG431SN', 'ZG5080K', 'ST123D']

# 나오는 차량들을 처음부터 확인하며
# 현재 차량의 인덱스(in_dict[out[i]])가
# 뒤에 나오는 차량들(out[j])의 인덱스(in_dict[out[j]])보다 큰 경우가 하나라도 존재한다면
# 추월한 것이므로 answer 1증가시키고 다음차량을 확인한다.
answer = 0
for i in range(N-1):
    for j in range(i+1, N):
        if in_dict[out[i]] > in_dict[out[j]]:
            answer += 1
            break

# in: A:0, B:1, C:2, D:3, E:4, F:5
# out: B D C A F E 의 경우
# C 는 그대로 3번째 입력, 3번째 출력 이어서 추월하지 않은 것 처럼 보이지만
# C 뒤에 A F E 중에 A 가 C 보다 뒤에 나오기 때문에 A 를 추월한 것으로 간주.
# 표현을 다르게 하면
# 원래 진입할때 앞에 있던 차들이 나보다 뒤에 나오면 추월했다는 것이기 때문에
# (A  B) C  D  E  F  / C 앞의 A, B 와
#  B  D  C (A  F  E) / C 뒤의 A, F, E 중에 겹치는게 있는 지 확인
print(answer)

