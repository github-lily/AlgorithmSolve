def solution(b, y):
    total = b + y
    h = 3
    while True :
        if total % h == 0 :
            w =  total // h
            if (w-2) * (h-2) == y :
                return [w,h]
        h += 1
    