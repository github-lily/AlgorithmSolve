N, M = map(int,input().split())

poketmons_num = {}      # key = 포켓몬 번호
poketmons_name = {}     # key = 포켓몬 이름

for i in range(1,N+1) :
    name = input()
    poketmons_num[i] = name
    poketmons_name[name] = i

for _ in range(M) :
    q = input()
    if q.isdigit() :    # 숫자로만 되어있다면
        print(poketmons_num[int(q)])
    else :
        print(poketmons_name[q])
