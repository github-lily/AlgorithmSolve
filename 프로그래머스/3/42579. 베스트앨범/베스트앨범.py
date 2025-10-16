from collections import defaultdict

def solution(genres, plays):
    
    songs = defaultdict(list)
    total_cnt = defaultdict(int)
    ans = []
    
    for i, cnt in enumerate(plays) :
        songs[genres[i]] += [(cnt, i)]
        total_cnt[genres[i]] += cnt
    
    # 1. 장르 구하기
    sort_cnt = sorted(total_cnt, key = lambda x : total_cnt[x], reverse = True)
    
    # 노래 구하기
    for g in sort_cnt :
        # 2. 장르 내 정렬
        # 주의! 재생수는 내림차순, 인덱스는 오름차순이므로 reverse = True 하면 인덱스 정렬에 문제생김!
        songs[g].sort(key=lambda x : (-x[0],x[1]))
        g_cnt = 0
        for song in songs[g] :
            ans.append(song[1])
            g_cnt += 1
            
            # 3. 장르별 최대 2곡 선택
            if g_cnt == 2 :
                break
                
    return ans


        
        
    