def solution(id_list, report, k):
    # report [0] : 신고자, [1] 신고 당한 사람
    ans = [0] * len(id_list)
    reports = {x:0 for x in id_list}
    
    # 신고 당한 횟수 카운트
    for r in set(report) :
        reports[r.split()[1]] += 1
    
    # 메일 발송 횟수 카운트
    for r in set(report) :
        send, recive = r.split()
        if reports[recive] >= k :
            ans[id_list.index(send)] += 1
    
    return ans