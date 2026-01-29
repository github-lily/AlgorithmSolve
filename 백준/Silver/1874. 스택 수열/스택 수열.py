import sys
input = sys.stdin.readline

n = int(input())
lst = list(int(input()) for _ in range(n))



def check():
    stack = []
    ans = []
    i = 0

    for num in range(1,n+1) :
        # stack에 추가
        stack.append(num)
        ans.append('+')

        # 수열과 비교 
        while i < n :
            if stack :
                if lst[i] == stack[-1] :
                    stack.pop()
                    i += 1
                    ans.append('-')
                elif lst[i] < stack[-1] :
                    return False
                else :
                    break
            else :
                break
    
    if not stack :
        return ans
    
    return False


result = check()

if not result :
    print("NO")
else :
    print("\n".join(result))


