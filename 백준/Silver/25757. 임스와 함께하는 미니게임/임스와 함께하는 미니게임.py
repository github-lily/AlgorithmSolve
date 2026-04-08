N,game = input().split()

people = set()

for _ in range(int(N)) :
    name = input()
    people.add(name)

cnt = len(people)

if game == "Y" :
    ans = cnt

elif game == "F" :
    ans = cnt // 2

elif game == "O" :
    ans = cnt // 3

print(ans)