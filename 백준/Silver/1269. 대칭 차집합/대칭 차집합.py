a,b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

AB = A-B
BA = B-A
ans = len(AB|BA)
print(ans)