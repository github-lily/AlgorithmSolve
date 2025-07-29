import sys
input = sys.stdin.readline

def check(i,j,size) :
    num = paper[i][j]
    for r in range(i,i+size) :
        for c in range(j,j+size) :
            if paper[r][c] != num :
                return False
    return True


def divide(r,c,size) :
    global minus, one, zero
    if check(r,c,size) :
        if paper[r][c] == 1 :
            one += 1
        elif paper[r][c] == 0 :
            zero += 1
        else :
            minus += 1
        return
    
    three_halves = size//3

    divide(r,c,three_halves)
    divide(r,c+three_halves,three_halves)
    divide(r,c+(three_halves*2),three_halves)

    divide(r+three_halves,c,three_halves)
    divide(r+three_halves,c+three_halves,three_halves)
    divide(r+three_halves,c+(three_halves*2),three_halves)

    divide(r+(three_halves*2),c,three_halves)
    divide(r+(three_halves*2),c+three_halves,three_halves)
    divide(r+(three_halves*2),c+(three_halves*2),three_halves)



N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]

zero = one = minus = 0

divide(0,0,N)

print(minus)
print(zero)
print(one)
