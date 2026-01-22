from collections import defaultdict

def solution(arr):
    
    dic = defaultdict(int)
    
    # 개수 카운트
    for a in arr :
        dic[a] += 1
    
    # 최빈값 cnt 찾기
    mx_cnt = max(dic.values())
    # 최빈값
    mx = 0
    cnt = 0     
    
    
    # 최빈값 원소 찾기
    for k,v in dic.items() :
        if v == mx_cnt :
            mx = k
            cnt += 1
            if cnt > 1 :
                return -1
    return mx

    
    

        
    