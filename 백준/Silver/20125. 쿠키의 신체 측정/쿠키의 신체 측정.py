
import sys
N = int(input())
input = sys.stdin.readline

coo = [input().strip() for _ in range(N)]


def findHeart() :
    for i in range(N) :
        for j in range(N) :
            if coo[i][j] == "*" :
                heart = (i+2,j+1)
                return heart



def findArms(r,c) :
    left = 0
    right = 0
    
    # 왼쪽 팔 시작점 찾기
    for j in range(N) :
        if coo[r][j] == "*" :
            left = c - j
            break

    # 우측 팔 끝점 찾기
    for j in range(N-1,-1,-1) :
        if coo[r][j] == "*" :
            right = j - c
            break
    
    return left, right

def findWaist(r,c) :
    cnt = 0
    i = r+1
    if coo[i][c] == "*" :
        while i<N and coo[i][c] == "*"  :
            cnt += 1
            i+= 1
    return cnt, i-1
            
def findLeg(r,c) :
    left = 0
    right = 0

    # 왼쪽다리
    i = r+1
    if coo[i][c-1] == "*" :
        while i<N and coo[i][c-1] == "*"  :
            left += 1
            i+= 1

    
    # 오른쪽다리
    i = r+1
    if coo[i][c+1] == "*" :
        while i<N and coo[i][c+1] == "*"  :
            right += 1
            i+= 1


    return left,right


heart = findHeart()
l_arm,r_arm = findArms(heart[0]-1, heart[1]-1)
waist, e_waist = findWaist(heart[0]-1, heart[1]-1)
l_leg, r_leg = findLeg(e_waist, heart[1]-1)



print(*heart)
print(l_arm,r_arm,waist,l_leg, r_leg)