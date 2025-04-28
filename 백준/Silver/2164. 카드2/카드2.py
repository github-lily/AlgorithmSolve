N = int(input())

from collections import deque
q = deque([x for x in range(1,N+1)])
pointer = 0


while q :

    if q :
        # 맨 첫번째 카드 버리기
        num = q.popleft()

        if q :
            # 두번째 카드 뽑아서 맨 뒤로 넣기기
            q.append(q.popleft())
        else :
            print(num)
        
