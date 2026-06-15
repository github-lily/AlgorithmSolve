
# 모든 달 28일까지
def solution(today, terms, privacies):
    # 총 일수로 변환 함수
    def change_date(date) :
        y, m, d = map(int, date.split("."))
        return y*12*28 + m *28 + d
    
    
    ans = []
    todate = change_date(today)
    
    # 달을 일자로 변경
    date_terms = {}      
    for term in terms :
        category, month = term.split()
        date_terms[category] = int(month) * 28


    for i in range(len(privacies)) :
        privacie = privacies[i]
        day, t = privacie.split()
        date = change_date(day)
        
        diff = todate - date
        if diff >= date_terms[t]  :
            ans.append(i+1)
        
    
    
    return ans
        
        
        
        
        
        
    