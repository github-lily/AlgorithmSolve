
import sys
input = sys.stdin.readline

def check(r,c,size) :
    color = arr[r][c]
    for i in range(r,r+size) :
        for j in range(c,c+size) :
            if arr[i][j] != color :
                return False
    return True

def divide(r,c,size) :
    global white, blue
    if check(r,c,size) :
        if arr[r][c] == 0 :
            white += 1
        else :
            blue += 1
        return
    
    half = size // 2
    divide(r, c, half)
    divide(r, c+half, half)
    divide(r+half, c, half)
    divide(r+half, c+half, half)




N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

white = 0
blue = 0

divide(0,0,N)

print(white)
print(blue)