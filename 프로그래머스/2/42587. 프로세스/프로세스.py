def solution(arr, target):
    order = 0
    orders = sorted(arr, reverse=True)
    cur = 0
    
    while True :
        for i, val in enumerate(arr) :
            if val == orders[cur] :
                cur += 1
                order += 1
                if i == target :
                    return order

    return order
    
    