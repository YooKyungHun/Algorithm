from collections import defaultdict

def solution(id_list, reports, k):
    # key: key 를 신고한 사람들
    report_dic = defaultdict(set)
    for report in reports:
        attacker, defender = map(str, report.split())
        report_dic[defender].add(attacker)
    # report_dic = {'frodo': {'apeach', 'muzi'}, 'neo': {'muzi', 'frodo'}, 'muzi': {'apeach'}}

    # key: key 가 받을 메일 수
    mailed_cnt = defaultdict(int)
    for key, value in report_dic.items():
        if len(value) >= k:
            for i in value:
                mailed_cnt[i] += 1
    # mailed_cnt = {'apeach': 1, 'muzi': 2, 'frodo': 1})

    answer = []
    for id_one in id_list:
        answer.append(mailed_cnt[id_one])

    return answer










