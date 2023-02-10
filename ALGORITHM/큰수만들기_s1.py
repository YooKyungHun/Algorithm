'''
큰 수 만들기_s1
- 구현(슬라이싱을 2번 이용하게 되면 시간 초과) => for 문으로 변경
- 가장 큰 수(max() 를 사용하면 시간 초과) => 직접 대소비교하고 9 나오면 가지치기
큰 수 만들기_s2 : 스택
- 좀 더 정석적인 방법
'''

def solution(number, k):
    answer = ''
    cnt = 0
    xxxxxxxxxxx = len(number) - k
    # cnt = 앞으로 구해야 할 글자 수
    cnt = xxxxxxxxxxx

    while len(answer) != xxxxxxxxxxx:
        cnt -= 1
        M = 0
        for i in range(len(number) - cnt):
            if number[i] == '9':
                M = '9'
                break
            tmp = int(number[i])
            if M < tmp:
                M = tmp

        M = str(M)
        idx = number.index(M)
        number = number[idx + 1:]

        answer += M

    return answer

'''
len(number) = 10, k = 4 라면 아무리 늦어도 number 의 앞 5 글자 중에서 맨 앞자리가 나와야 함.
그래야 len(return) = 10 - 4 = 6 을 맞출 수 있음.
만약 앞 5 글자가 아닌 뒤 5글자 중에서 return 의 맨 앞자리가 나온다면,
len(return) 이 6글자를 맞출 수가 없게 됨

number      k  cnt
4177252841  4  6  => 앞에서부터 len(number) - (cnt - 1) 중(41772)에서 가장 큰 수 => 7
7252841     4  5  => 앞에서부터 len(number) - (cnt - 1) 중(725)  에서 가장 큰 수 => 7
252841      4  4  => 앞에서부터 len(number) - (cnt - 1) 중(252)  에서 가장 큰 수 => 5
2841        4  3  => 앞에서부터 len(number) - (cnt - 1) 중(28)   에서 가장 큰 수 => 8
41          4  2  => 앞에서부터 len(number) - (cnt - 1) 중(4)    에서 가장 큰 수 => 4
1           4  1  => 앞에서부터 len(number) - (cnt - 1) 중(1)    에서 가장 큰 수 => 1  
'''