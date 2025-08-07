N,K = map(int,input().split())

lst = [x for x in range(N+1)]

for a in range(2,N+1) :
    if lst[a] :
        for b in range(a,N+1,a) :
            if lst[b] :
                lst[b] = 0
                K -= 1
                if not K :
                    print(b)
                    exit()
            
