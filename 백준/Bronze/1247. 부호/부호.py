
for _ in range(3) :
    N = int(input())
    sum_val = 0
    for _ in range(N) :
        num = int(input())
        sum_val += num
    
    if sum_val > 0 :
        print('+')
    elif sum_val == 0 :
        print("0")
    else :
        print("-")

    