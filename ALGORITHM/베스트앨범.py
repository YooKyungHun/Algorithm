from collections import defaultdict


def solution(genres, plays):
    answer = []

    sum_dic = defaultdict(int)
    test_dic = defaultdict(list)
    idxs = [i for i in range(len(plays))]

    # 1. 장르별 play 의 합계 구하기
    # 2. 각 곡별로 (인덱스, 장르, 재생 수) 구하기
    for genre, play, idx in zip(genres, plays, idxs):
        sum_dic[genre] += play
        test_dic[genre].append((idx, genre, play))

    # sum_dic = {'classic': 1450, 'pop': 3100}
    # test_dic = {'classic': [(0, 'classic', 500), (2, 'classic', 150), (3, 'classic', 800)], 'pop': [(1, 'pop', 600), (4, 'pop', 2500)]}

    # 3. # 1 의 결과를 이용해서 장르별 합계 정렬하기
    tmp = []
    for idx, value in sum_dic.items():
        tmp.append([idx, value])
    # tmp = [['classic', 1450], ['pop', 3100]]

    tmp.sort(key=lambda x: -x[1])
    # tmp = [['pop', 3100], ['classic', 1450]]

    for genre, _ in tmp:
        a = sorted(test_dic[genre], key=lambda x: (-x[2], x[0]))
        # a = [(3, 'classic', 800), (0, 'classic', 500), (2, 'classic', 150)]

        answer.append(a[0][0])

        if len(a) >= 2:
            answer.append(a[1][0])

    return answer

