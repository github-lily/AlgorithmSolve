from collections import defaultdict

def solution(arr):
    arr.sort()
    
    dic = defaultdict(int)
    lst = []
    
    # 개수 카운트
    for a in arr :
        dic[a] += 1
    
    mx = max(dic.values())
    
    # 최대값 원소 찾기
    for k,v in dic.items() :
        if v == mx :
            lst.append(k)
    
    # 최빈값 반환
    if len(lst) > 1 :
        return -1
    else :
        return lst[0]
    
    

        
    