
def find(H,W,N) :
    cnt = 0
    for j in range(W) :
        for i in range(H) :
            cnt += 1
            if cnt == N :
                room = (i+1)*100 + (j+1)
                print(room)
                return



import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    h,w,n = map(int,input().split())

    find(h,w,n)
