# 가장 큰 숫자 만들기
# 같은 순위의 연산자 수는 없음. 2개면 2!개
# 음수면 절대값으로 비교

def solution(expression):
    mx = 0
    n = len(expression)
    signs = ["+", "-", "*"]
    
    # 문자, 숫자 분리 저장
    exps = []
    left = 0
    right = 0
    while True :
        # 종료조건
        if right == n :
            exps.append(int(expression[left:]))
            break
        
        # 숫자면 패스
        if expression[right].isdigit() :
            right += 1
            
        # 기호 만나면 저장
        else :
            exps.append(int(expression[left : right]))   # 숫자 추가
            exps.append(expression[right])          # 기호 추가
            right += 1
            left = right
    
    # 우선순위대로 계산해주는 함수
    def cal(origin, sign) :
        stack = []
        i = 0
        while i < len(origin) :
            cur = origin[i]
            if cur == sign :
                pre = stack.pop()
                post = origin[i+1]
                if sign == "+" :
                    stack.append(pre + post)
                elif sign == "-" :
                    stack.append(pre - post)
                else :
                    stack.append(pre * post)
                i += 2
                
            else :
                stack.append(cur)
                i += 1
                
        return stack

    
    # 우선순위대로 계산
    for i in range(3) :
        for j in range(3) :
            if i == j :
                continue
            for k in range(3) :
                if i != j and j != k and i != k :
                    temp1 = cal(exps,signs[i])
                    temp2 = cal(temp1, signs[j])
                    temp3 = cal(temp2, signs[k])
                    
                    if mx < abs(temp3[0]) :
                        mx = abs(temp3[0])
    
    return mx


        
    
    