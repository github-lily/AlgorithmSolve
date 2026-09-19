def solution(brown, yellow):
    summ = brown + yellow
    h = 3
    
    while h * h <= summ :
        if summ % h == 0 :
            w = summ // h
            if (w-2) * (h-2) == yellow :
                return [w,h]
        
        h += 1
        