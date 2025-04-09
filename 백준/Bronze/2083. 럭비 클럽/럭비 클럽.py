members = []
while True :
    name, age, weight = input().split()

    if int(age) == 0 :
        break

    if int(age) > 17 or int(weight) >= 80 :
        members.append((name, "Senior"))
    else : 
        members.append((name,"Junior"))

for member in members :
    print(*member)
