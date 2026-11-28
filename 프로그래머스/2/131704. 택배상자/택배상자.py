
def solution(order):
    n = len(order)
    stack = []
    cnt = 0
    idx = 1
    
    for target in order :
        while True :
            if idx == target :
                cnt += 1
                idx += 1
                break
            
            else :
                if stack :
                    if stack[-1] == target :
                        stack.pop()
                        cnt += 1
                        break
                    else :
                        # 종료 조건 : 스택 상단과 다른데, 순서도 지남
                        if idx > target :
                            return cnt
                stack.append(idx)
                idx += 1
            
                    

    return cnt