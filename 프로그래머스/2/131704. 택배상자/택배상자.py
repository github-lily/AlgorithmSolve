
def solution(order):
    stack = []
    cnt = 0
    idx = 1
    
    for target in order :
        while True :
            # 메인 컨베이너에서 적재
            if idx == target :
                cnt += 1
                idx += 1
                break
            
            # 보조 컨베이너에서 적재
            elif stack and stack[-1] == target :
                stack.pop()
                cnt += 1
                break
                

            # 종료 조건 : 스택 상단과 다른데, 순서도 지남
            elif idx > target :
                return cnt
            
            # 보조 컨베이너에 보관
            stack.append(idx)
            idx += 1
            
                    

    return cnt