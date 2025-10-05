def solution(brown, yellow):
    total = brown + yellow
    
    h = 3
    
    while h*h <= total :            # h*h보다 커지면 중복탐색임([2,4][4,2], [3,3]...)
        if total % h == 0 :         # h의 약수여야지만 사각형 만들기 가능
            w = total // h
            if (w-2) * (h-2) == yellow :
                return [w,h]

        h += 1
        
