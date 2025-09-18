def solution(array, commands):
    answer = []
    for i,j,k in commands :
        array1 = sorted(array[i-1:j])
        answer.append(array1[k-1])
    
    return answer