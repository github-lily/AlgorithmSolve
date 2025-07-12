N = int(input())

for i in range(1,N+1) :
    ans = ("*" * i) + (" "* (N-i)) + (" "* (N-i)) + ("*" * i)
    print(ans)

for k in range(1,N+1) :
    ans2 = ("*" * (N-k)) + (" "* k) + (" "* k) + ("*" * (N-k))
    print(ans2)