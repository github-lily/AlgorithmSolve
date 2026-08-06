def solution(s):
    zero = 0
    cnt = 0
    
    while s and s != "1" :
        n = len(s)
        one = s.count("1")
        zero += (n - one)

        s = bin(one)[2:]        #ob1010
        cnt += 1
    
    return [cnt,zero]
    
    