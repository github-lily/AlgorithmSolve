def push(x) :
    heap.append(x)

    i = len(heap)-1
    while i > 1 and heap[i] < heap[i//2] :          # 부모보다 작으면 위치 바꾸기
        heap[i],heap[i//2] = heap[i//2], heap[i]
        i = i//2
    
def pop() :
    if len(heap) == 1 :
        return 0            # 0은 인덱스 위해 넣어둔 것. 그것만 있으면 비어있는 heap
    
    root = heap[1]          # 최솟값
    heap[1] = heap[-1]      # 맨 뒷 값 가져오기
    heap.pop()              # 맨 뒷 값 제거

    # 정렬
    i = 1

    while True :
        smallest = i
        left = i * 2        # 왼쪽 자식
        right = i * 2 + 1   # 오른쪽 자식

        # 왼쪽 오른쪽 자식과 값 비교하며 최소값이 부모 노드(현재 위치)에 오도록
        if left < len(heap) and heap[left] < heap[smallest] :   
            smallest = left
        if right < len(heap) and heap[right] < heap[smallest] :
            smallest = right
        
        if smallest == i :
            break           # 부모 노드가 가장 작은 값이면 종료

        # 가장 작은 값과 부모 교체
        heap[smallest], heap[i] = heap[i], heap[smallest]
        i = smallest        # 작은 값과 교체된 인덱스의 값 다시 정렬 시작      

    return root



N = int(input())
heap = [0]
ans = []
for _ in range(N) :
    x = int(input())
    if x == 0 :
        num = pop()
        ans.append(num)
    else :
        push(x)

        
print("\n".join(map(str,ans)))