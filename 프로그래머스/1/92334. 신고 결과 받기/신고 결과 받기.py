# 신고 하기
# K번 이상 신고당하면 정지, 메일 발송
# 결과 메일 수

def solution(id_list, report, k):
    report_recive = {}
    mail_recive = {}
    
    for id in id_list :
        report_recive[id] = set()
        mail_recive[id] = 0
        
    for rep in report :
        send, recive = rep.split()
        report_recive[recive].add(send)
    

    for name, sends in report_recive.items() :
        if len(sends) >= k :
            for s in sends :
                mail_recive[s] += 1
    
    ans = []
    for id in id_list :
        ans.append(mail_recive[id])
        
    return ans
            
    