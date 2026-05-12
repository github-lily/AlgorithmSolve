from collections import deque
# 가능한 단어를 q에 넣고 방문 표시 하며 비교

def check(now, nxt) :
    diff = 0
    for i in range(len(now)) :
        if diff > 1 :
            return False
        if now[i] != nxt[i] :
            diff += 1
    if diff == 1 :
        return True     # 하나만 다르면 통과
    else :
        return False    # 같은 단어는 거르기

def solution(begin, target, words):
    
    if target not in words :
        return 0
    
    v = set()
    q = deque([(begin,0)])
            
    
    while q :
        cur, count = q.popleft()
        if cur == target :
            return count
        
        for word in words :
            if word not in v and check(cur,word) :
                q.append((word,count+1))
                v.add(word)

    
    return 0
            
    
    