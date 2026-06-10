def solution(records):
    users = {}
    result = []
    for record in records :
        rec = record.split()
        act, uid = rec[0], rec[1]
        if act == 'Enter' :
            name = rec[2]
            users[uid] = name
            result.append((uid, '님이 들어왔습니다.'))
        elif act == 'Change' :
            name = rec[2]
            users[uid] = name
        else :
            result.append((uid, '님이 나갔습니다.'))
    
    ans = []
    for res in result :
        ans.append(users[res[0]] + res[1] )
    
    return ans
            
        