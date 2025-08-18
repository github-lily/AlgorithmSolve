import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

tails = [lst[0]]
for num in lst[1:] :
    if tails[-1] < num :    # 현재 꼬리값보다 크면 추가
        tails.append(num)
    
    else :
        # 현재 꼬리값보다 작거나 같을 경우 꼬리값리스트 중 들어갈 위치 탐색
        left =  0
        right = len(tails) -1       # 인덱스값이니 -1
        
        while left < right :
            mid = (left + right) // 2

            # num 이 중간값보다 큰 경우 그 위치+1을 좌측끝값으로 설정 
            # if tails[mid] > num : right = mid-1 else : left = mid 로 설정할 경우 
            # left = mid 값이 같아졌을 때 무한루프에 빠짐 
            if tails[mid] < num :   
                left = mid + 1
            else :
                right = mid
        
        # 위치 찾으면 num 값 후보에 넣기
        tails[left] = num

print(len(tails))
