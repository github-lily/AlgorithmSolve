def solution(record):
    udict = {}
    orders = []
    result = []
    
    # 닉네임 저장
    for rec in record :
        if rec.split()[0] == 'Leave' :
            orders.append(('L', rec.split()[1]))
        else :
            com, uid, name = rec.split()
            if com == 'Enter' :
                udict[uid] = name
                orders.append(('E', uid))

            else :  # Change
                udict[uid] = name
    
    # 메시지 생성
    for order in orders :
        typ, uid = order
        if typ == 'E' :
            result.append(f'{udict[uid]}님이 들어왔습니다.')
        else :
            result.append(f'{udict[uid]}님이 나갔습니다.')
            
    return result
        
            
            
            