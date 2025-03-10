
plate = input()
N = len(plate)
h = 10

for i in range(1,N) :
    if plate[i-1] == plate[i] :
        h += 5
    else :
        h += 10

print(h)