from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        
        for w in words:
            diff = sum(a != b for a, b in zip(word, w))
            if diff == 1:
                q.append((w, cnt + 1))
                words.remove(w)
                break
                
    return 0
