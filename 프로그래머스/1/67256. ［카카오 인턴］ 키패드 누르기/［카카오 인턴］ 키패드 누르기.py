def solution(numbers, hand):
    # 키패드 좌표 dict 만들기
    keypad = {}
    x = 1
    while x < 10 :
        for i in range(3) :
            for j in range(3) :
                keypad[x] = (i,j)
                x += 1
                
    keypad['*'] = (3,0)
    keypad[0] = (3,1)
    keypad['#'] = (3,2)
    
    
    # 손이 정해진 숫자 set 만들기
    left_num = {1,4,7}
    right_num = {3,6,9}
    
    
    # 절대값 차이 계산 식
    def cal_diff(l,r,n) : # 왼손, 오른손, 가야할 위치
        
        li,lj = keypad[l]
        ri,rj = keypad[r]
        ni,nj = keypad[n]
        
        l_diff = abs(li-ni) + abs(lj-nj)
        r_diff = abs(ri-ni) + abs(rj-nj)
        
        return l_diff, r_diff
    
    # 순회하며 기록(2,5,8,0 은 키패드 좌표에서 절대값 차이로 계산)
    left = '*'
    right = '#'
    ans = ""
    
    for num in numbers :
        if num in left_num :
            left = num
            ans += 'L'
        elif num in right_num :
            right = num
            ans += 'R'
        else :
            left_diff, right_diff = cal_diff(left, right, num) 
            if left_diff < right_diff :     # 왼손이 더 가까움
                left = num
                ans += 'L'
            elif right_diff < left_diff :   # 오른손이 더 가까움
                right = num
                ans += 'R'
            else :      # 거리가 같을 경우
                if hand == 'left' :
                    left = num
                    ans += 'L'
                else :
                    right = num
                    ans += 'R'
                    
    return ans
                