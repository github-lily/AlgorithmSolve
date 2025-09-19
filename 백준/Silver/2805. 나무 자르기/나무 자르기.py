N,K = map(int,input().split())
trees = list(map(int,input().split()))

mx = 0

def cutting(h) :
    amount = 0
    for t in trees :
        amount += max(0,t-h)
    return amount


def binary(s,e) :
    global mx

    if s > e :
        return
    
    mid = (s+e)//2
    amount = cutting(mid)
    if amount >= K :
        if mx < mid :
            mx = mid
        return binary(mid+1,e)
    else :
        binary(s,mid-1)


binary(0,max(trees))

print(mx)
