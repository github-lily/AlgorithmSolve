import math
# 차량별 누적 주차 시간을 계산하여 요금 일괄 정산
# 초과한 시간은 올림
# 차량 번호 기준 오름차순

def solution(fees, records):
    cars = {}
    results = []
    
    # 분으로 변환
    def to_min(t) :
        h,m = map(int,t.split(":"))
        return h*60 + m
        
    # 차량 시간 기록
    for record in records :
        time, car, typ = record.split()
        mn = to_min(time)
        if car not in cars :
            cars[car] = []
        cars[car].append((typ, mn))
    
    # 누적 시간 & 요금 계산
    for key, vals in cars.items() :
        temp = 0
        # 입출차 모두 이루어짐
        N = len(vals)
        if N % 2 == 0 :
            for i in range(1,N,2) :
                temp += vals[i][1] - vals[i-1][1]
        # 출차 없음
        else :
            for i in range(1,N-1,2) :
                temp += vals[i][1] - vals[i-1][1]
            # 23:59 기준 계산
            end = 23*60 + 59
            temp += end - vals[-1][1]
        
        # fee = 기본요금[1] + ceil((누적 시간 - 기본 시간[0]) / 단위 시간[2]) * 단위 요금[3]
        if temp <= fees[0] :        # 기본시간 미만 사용
            fee = fees[1]
        else :
            fee = fees[1] + math.ceil((temp - fees[0]) / fees[2]) * fees[3]
            
            
        results.append((key, fee))
    
    # 정답
    results.sort()
    ans = [x[1] for x in results]
    return ans