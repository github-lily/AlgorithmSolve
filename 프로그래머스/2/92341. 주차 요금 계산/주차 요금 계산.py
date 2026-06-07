import math

def solution(fees, records):

    # 시간 계산 함수
    def time_cal(start,end) :
        sh,sm = map(int, start.split(':'))
        eh,em = map(int, end.split(':'))
        
        start_min = sh * 60 + sm
        end_min = eh * 60 + em
        
        res = end_min - start_min
        
        return res
    
    
    # 주차 요금 계산 함수
    def fee_cal(t) :
        fee = fees[1]
        # 기본요금[1] + ((이용시간 - 기본시간[0])/단위시간[2]) * 단위요금[3]
        if t > fees[0] :    # 기본시간 이상 이용 시에만 계산
            fee += (math.ceil((t - fees[0]) / fees[2])) * fees[3]
        return fee
    
    # 차량별 기록 저장
    cars = {}
    
    for record in records :
        time, num, rec = record.split()
        if not cars.get(num) :
            cars[num] = []
        cars[num].append(time)
    
    # 차량별 요금 계산
    total_fees = []
    for car in cars :
        tmp = cars[car]
        money = 0
        total_time = 0
        N = len(tmp)
        
        # 출차 기록 있을 때
        if N % 2 == 0 : 
            for i in range(1,N,2) :
                total_time += time_cal(tmp[i-1], tmp[i])

                
        # 출차 기록 없을 때
        else :
            for i in range(1,N-1,2) :
                total_time += time_cal(tmp[i-1], tmp[i])
            total_time += time_cal(tmp[N-1], '23:59')
        
        # 누적 시간으로 요금 계산
        money += fee_cal(total_time) 
        total_fees.append([car, money])
    
    # 정렬 :차량 번호 올림차순
    total_fees.sort()
    result = []
    for total_fee in total_fees :
        result.append(total_fee[1])
    
    return result
                
                
        
    