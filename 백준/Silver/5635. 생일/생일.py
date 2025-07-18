n = int(input())
people = []

for _ in range(n):
    name, day, month, year = input().split()
    day = int(day)
    month = int(month)
    year = int(year)
    people.append((year, month, day, name))

people.sort()

print(people[-1][3])  # 가장 어린 사람
print(people[0][3])   # 가장 나이 많은 사람
