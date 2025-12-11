def solution(n):
    cnt = bin(n).count("1")
    x = n+1
    while True :
        if bin(x).count("1") == cnt :
            return x
        x += 1