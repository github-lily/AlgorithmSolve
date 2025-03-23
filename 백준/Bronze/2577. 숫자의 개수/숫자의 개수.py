
a = int(input())
b = int(input())
c = int(input())

num_lst = [0]*10
x = str(a * b * c)
for i in range(len(x)) :
    num_lst[int(x[i])] += 1

for num in num_lst :
    print(num)