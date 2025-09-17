
import heapq
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
q = []

flag = False
for i in range(N) :
    for j in range(N) :
        # N까지 채우기
        if flag == False :
            if len(q) < N :
                heapq.heappush(q,arr[i][j])
            else :
                flag = True
        # 모든 원소가 찼으면
        else :
            num = heapq.heappop(q)
            if arr[i][j] > num :
                heapq.heappush(q,arr[i][j])
            else :
                heapq.heappush(q,num)

print(q[0])
            