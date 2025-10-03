def solution(numbers):
    # 만들 수 있는 수 모두 구하기
    numbers = sorted(map(int,numbers))
    primes = set()
    N = len(numbers)
    v = [0]*N
    ans = 0
    
    def is_prime(num) :
        if num < 2 :
            return False
        
        if num % 2 == 0 :
            if num == 2 :
                return True
            return False
        
        
        i = 3
        while i*i <= num :
            if num % i == 0 :
                return False
            i += 2 
        
        return True
    

    def dfs(n, new_num) :
        nonlocal N
        
        if n == N :
            return
        
        for i in range(N) :
            if v[i] == 1 :
                continue
            
            # 중복된 숫자 거르는 부분
            # [1,1,7] 일 때, 앞에 1이 안쓰였으면 뒤의 1도 안씀
            # 사용할 경우 [1,7](첫번째 1사용) , [1,7] (두번째 1 사용) 중복된 값이 나올 수 있음.
            if i > 0 and numbers[i] == numbers[i-1] and v[i-1] == 0 :
                continue
                
            v[i] = 1
            next_num = new_num*10 + numbers[i]
            
            if is_prime(next_num) :
                primes.add(next_num)
                
            
            dfs(n+1,next_num)
            v[i] = 0
                
            
    dfs(0,0)
    ans = len(primes)
    return ans

    
    