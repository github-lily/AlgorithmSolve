N = int(input())

member = []
for i in range(N) :
    age,name = input().split()
    member.append((int(age),name, i+1))

member.sort(key = lambda x : (x[0], x[2]))

for person in member :
    print(person[0], person[1])