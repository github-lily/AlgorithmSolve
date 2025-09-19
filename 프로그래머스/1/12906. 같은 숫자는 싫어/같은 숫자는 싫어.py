from collections import deque
def solution(arr):
    q = [arr[0]]
    for i in range(1,len(arr)) :
        if arr[i-1] != arr[i] :
            q.append(arr[i])
    
    return q
    