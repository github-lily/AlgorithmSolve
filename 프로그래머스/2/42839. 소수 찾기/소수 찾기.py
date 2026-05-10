def solution(numbers):
    cnt = 0
    nums = set()
    N = len(numbers)
    v = [False] * N
          
        
    def make_num(num) :
        if num :
            nums.add(int(num))
        
        for i in range(N) :
            if v[i] :
                continue
            
            v[i] = True
            make_num(num + numbers[i])
            v[i] = False
            
    
    make_num("")
    
    for num in nums :
        if check_prime(num) :
            cnt += 1
    
    return cnt
        
    
def check_prime(num) :
    if num < 2 :
        return False
    if num % 2 == 0 :
        if num == 2 :
            return True
        return False
    
    # 121 = 11*11 같은 경우 고려 제곱근 나누기
    for i in range(3, int(num**0.5) + 1,2) :       
        if num % i == 0 :
            return False
    
    return True
