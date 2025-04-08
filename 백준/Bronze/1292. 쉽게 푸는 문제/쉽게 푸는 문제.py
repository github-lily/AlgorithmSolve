num_lst = []
for i in range(1,46) :
    num_lst += [i]*i


n,m = map(int,input().split())


print(sum(num_lst[n-1:m]))
