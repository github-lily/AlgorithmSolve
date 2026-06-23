def solution(msg):
    ans = []
    
    # 사전 만들기
    dic = {}
    idx = 1       # 색인 번호
    while idx < 27 :
        dic[chr(64+idx)] = idx
        idx+= 1
    
    n = len(msg)
    p = 0
    # 사전에 없는 단어 나올때까지 글자수 늘려가며 확인(일치하는 가장 긴 문자열 찾기)
    k = p+1
    while k < n+1 :
        if msg[p:k+1] in dic :
            k += 1

            
        # 사전에 없는 단어만나면 현재 입력(w) 저장, w+c 사전 추가, 다음 확인
        else :
            w = msg[p:k]
            ans.append(dic[w])
            
            nxt = w + msg[k]        # c
            dic[nxt] = idx
            idx += 1
            
            p = k
            k = p+1
            
    if p < n :
        ans.append(dic[msg[p:]])
    
    return ans
            
            
    
        
