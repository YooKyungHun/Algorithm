def solution(n, k, e):
    answer,m = 0,0
    l=[]

    if len(e) <= k: return len(e)

    for i in range(len(e)):
        # 적군이 더 많아서, 무조권을 쓸지, 병사를 쓸지 결정해야함
        if n < e[i]:
            # 예전에 적군이 지금보다 많았는데, K 를 사용하지 않았어
            # => 그때 K 를 사용한거로 치고, 많은 병사를 받아오자
            # => 그리고 지금 적군을 상대할때 적은 병사를 사용하자
            if len(l) != 0 and max(l) > e[i] and k >= 1:
                n += max(l) - e[i]
                l.remove(max(l))
                l.append(e[i])
                k -= 1

            # 지금 적군이 더 많으면 그냥 K 사용하자
            elif k >= 1 and (len(l) == 0 or max(l) <= e[i]) :
                k -= 1

            # 종료조건: 적이 내 병사보다 많은데, K == 0 이야
            elif k == 0:
                return answer

        # 우리 병사가 더 많아서 그냥 병사 사용
        else:
            n = n - e[i]
            l.append(e[i])


        answer+=1
    return answer

# enemy  N  K  heap
#        7  3
# 4      3     [-4]
# 2      1     [-2, -4]
# 4      1  2
# 5      1  1
# 3      2     [-2, -3, -4] 중에서 heappop(heap) 을 통해 -4 를 다시 살려와서 ( 1 - 3 = -2 ) - (-4)
#           => [-2, -3]
# 3
# 1


# print(solution(2, 4, [3,3,3,3]))
# # 4
print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# 5
# print(solution(7, 3, [5, 5, 5, 5, 2, 3, 1]))
# ans : 5
# print(solution(1, 6, [2, 2, 2, 2, 3, 3, 1]))
# # ans : 7
# print(solution(10, 1, [2, 2, 2, 2, 2, 10]))
# # ans : 6
# print(solution(10, 1, [2, 2, 2, 2, 10]))
# # ans : 5