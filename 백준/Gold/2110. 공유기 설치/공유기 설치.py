
import sys
input = sys.stdin.readline

n, c = map(int,input().split())
houses = []
for _ in range(n) :
    houses.append(int(input()))

if n == 2 :
    ans = max(houses) - min(houses)
    print(ans)
    exit()

houses.sort()

start = 1                           # 최소 간격 
end = houses[-1] - houses[0]        # 최대 간격
mx = 0

while start <= end :
    mid = (start+end) // 2
    cur = houses[0]
    cnt = 1     # 하나 설치하고 시작

    # 임의의 gap(mid) 이상씩 간격 두면서 맨 앞부터 공유기 설치해보기
    for i in range(1,n) :
        if houses[i] >= cur + mid :
            cnt += 1
            cur = houses[i]
        
        # 가지치기. 공유기 개수 이상이면 gap 여유있단거니까 중단
        if cnt > c :
            break

    # 공유기 개수가 여유있다는 건 간격이 더 넓어도 된단 뜻        
    if cnt >= c :           
        mx = mid
        start = mid + 1

    else :
        end = mid - 1

print(mx)
            