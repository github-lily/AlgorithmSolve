# 순서 고정한 채로 숫자만 제거
# 뒤의 수가 더 크면 삭제?
def solution(number, k):
    n = len(number)
    stack = []

    
    for num in number :
        while stack and stack[-1] < num and k > 0 :
            stack.pop()     # 작은 값 제거
            k -= 1          # 제거 개수 차감
        stack.append(num)   # 작은 값 모두 제거 후 값 추가

    if k :
        return "".join(stack[:-k])
    return "".join(stack)
        