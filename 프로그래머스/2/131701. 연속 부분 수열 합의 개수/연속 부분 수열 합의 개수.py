def solution(elements):
    total = set()
    n = len(elements)
    double = elements + elements

    
    for k in range(1,n+1) : # 연속 부분 수열의 길이
        for i in range(n+k) :
            total.add(sum(double[i:i+k]))
    
    return len(total)
        