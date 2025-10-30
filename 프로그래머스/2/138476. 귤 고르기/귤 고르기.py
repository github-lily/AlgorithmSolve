from collections import defaultdict

def solution(k, fruits):
    f_cnt = defaultdict(int)
    
    # 과일 개수 카운트
    for fruit in fruits :
        f_cnt[fruit] += 1
    
    # 과일 많은 개수별로 정렬(과일 종류는 필요 없으므로 values만 사용)
    only_cnt = list(f_cnt.values())
    only_cnt.sort(reverse=True)

    # 과일 개수 많은 것부터 더해가면서 k와 비교
    total = 0
    ans = 0
    for cnt in only_cnt :
        if total + cnt < k :
            total += cnt
            ans += 1
        elif total+cnt >= k :
            ans += 1
            return ans

        
    