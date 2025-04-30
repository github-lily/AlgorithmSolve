
import sys
input = sys.stdin.readline




N = int(input())
stack = []
for _ in range(N) :
    cmd = input().strip().split()

    # push 인 경우
    if len(cmd) == 2 :
        stack.append(cmd[1])
    else :
        text = cmd[0]
        if text == "pop" :
            if stack :
                print(stack.pop())
            else :
                print(-1)    
        
        elif text == "size" :
            print(len(stack))
        
        elif text == "empty" :
            if stack :
                print(0)
            else :
                print(1)
        else :
            if stack :
                print(stack[-1])
            else :
                print(-1)