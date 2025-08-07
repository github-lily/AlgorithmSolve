import sys
input = sys.stdin.readline

N,K = map(int,input().split())

lst = [False] * (N+1)
cnt = 0
flag = False

for i in range(2,N+1) :
    if flag == True :
        break

    if lst[i] == False : # 아직 제거되지 않은 수
        lst[i] = True   # 방문표시
        cnt += 1

        if K == cnt :
            print(i)
            break

        else :
            for x in range(2, (N//i)+1) :
                if lst[i*x] == False :
                    lst[i*x] = True
                    cnt += 1
                    if K == cnt :
                        flag =True
                        print(i*x)
                        break