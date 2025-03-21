n = int(input())
lst = sorted(map(int,input().split()))


ans = lst[0] * lst[-1]
print(ans)
