def binary(s,e,target,lst) :

    include = False
    while s <= e :
        mid = (s+e) // 2
        
        if mid >= N :
            return False
        
        if lst[mid] == target :
            include = True
            return include
    
        elif lst[mid] < target :
            s = mid + 1
        
        else :
            e = mid -1
    
    return include


N = int(input())
lst = sorted(list(map(int,input().split())))

M = int(input())
targets = list(map(int,input().split()))


for t in targets :
    if binary(0,N,t,lst) :
        print(1)
    else :
        print(0)     
