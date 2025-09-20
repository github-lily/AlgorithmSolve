from collections import Counter

N,K = map(int,input().split())
trees = Counter(map(int,input().split()))

def solution(k,trees) :
    
    lo = 0
    hi = max(trees)
    mx = 0
    
    while lo+1 < hi :
        mid = (lo + hi)//2
        amount = cutting(trees,mid)

        if amount >= k :
            lo = mid
            if mx < mid :
                mx = mid
        
        else :
            hi = mid
    
    return mx


def cutting(trees,h) :
    amount = 0
    for t,n in trees.items() :
        if t>h :
            amount += (t-h)*n
    return amount


mx = solution(K,trees)
print(mx)
