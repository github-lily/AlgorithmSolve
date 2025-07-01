import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input()) 

left = 1              
right = M             
move = 0             

for _ in range(J):
    apple = int(input())
    if apple < left:
        diff = left - apple
        move += diff
        left -= diff
        right -= diff
    elif apple > right:
        diff = apple - right
        move += diff
        left += diff
        right += diff

print(move)
