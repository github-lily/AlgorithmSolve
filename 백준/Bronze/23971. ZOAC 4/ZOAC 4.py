h,w,n,m = map(int,input().split())

i = ((h-1)//(n+1)) +1
j = ((w-1)//(m+1)) +1
ans = i*j

print(ans)