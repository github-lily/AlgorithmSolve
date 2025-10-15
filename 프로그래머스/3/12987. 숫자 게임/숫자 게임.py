

def solution(A, B):
    
    score = 0
    A.sort()
    B.sort()
    v = [0] * len(B)

    i = j = 0
    
    while i <= j and j < len(B) :
        if A[i] < B[j] and v[j] == 0 :
            score += 1
            v[j] += 1
            i += 1
        j += 1
        
    return score

        