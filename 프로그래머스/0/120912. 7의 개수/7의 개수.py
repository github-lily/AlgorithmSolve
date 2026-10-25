def solution(array):
    cnt = 0
    array = map(str,array)

    for a in array :
        cnt += a.count("7")
    return cnt