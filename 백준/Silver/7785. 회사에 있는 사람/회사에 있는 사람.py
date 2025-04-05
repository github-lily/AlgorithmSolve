N = int(input())

work = set()
for _ in range(N) :
    list = input().split()
    if list[1] == 'enter' :
        work.add(list[0])
    else :
        work.remove(list[0])

sort_work = sorted(work,reverse=True)

for name in sort_work:
    print(name)