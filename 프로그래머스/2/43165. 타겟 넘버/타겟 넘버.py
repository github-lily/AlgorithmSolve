

        

def solution(numbers, target):
    N = len(numbers)
    
    def dfs(n, v, cnt) :
        if n == N :
            if v == target :
                cnt += 1
            return cnt

        cnt = dfs(n+1, v-numbers[n], cnt)
        cnt = dfs(n+1, v+numbers[n], cnt)
        
        return cnt
    
    answer = dfs(0,0,0)
    
    
    return answer