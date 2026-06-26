def solution(elements):
    total = set()
    n = len(elements)
    
    for i in range(n) : # 기준점
        ssum = elements[i]
        total.add(ssum)
        for j in range(i+1,i+n) :   # 2개, 3개... n개까지 더하기
            ssum += elements[j%n]
            total.add(ssum)
    
    return len(total)
        
        