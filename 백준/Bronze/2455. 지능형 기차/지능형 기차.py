
in_train = 0
mx_train = 0

for _ in range(4) :
    get_off, get_on = map(int,input().split())

    in_train -= get_off
    in_train += get_on

    if mx_train < in_train :
        mx_train = in_train
    

print(mx_train)
