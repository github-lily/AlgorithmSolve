from collections import Counter

def solution(k, tangerine):
    cnt = sorted(Counter(tangerine).values(), reverse=True)
    
    total = 0
    for i, n in enumerate(cnt):
        total += n
        if total >= k:
            return i + 1