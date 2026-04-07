import heapq

N = int(input())
lst = []
ans = []
for _ in range(N) :
    x = int(input())
    if x == 0 :
        if lst :
            num = heapq.heappop(lst)
            ans.append(num)
        else :
            ans.append(0)
    else :
        heapq.heappush(lst,x)

        
print('\n'.join(map(str,ans)))